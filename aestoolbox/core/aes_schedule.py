"""
This implementation is derived in part from the reference
Golang AES implementation, which carries the following notice:

Copyright (c) 2009 The Go Authors. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

   * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution.
   * Neither the name of Google Inc. nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import logging
from pprint import pprint
from aestoolbox.core.const import Sbox, powx, td0, td1, td2, td3

LOG = logging.getLogger(__name__)


class KeySchedule:
    def __init__(self, key, dec=False):
        self.key = key
        self.dec = dec
        self.xk = []
        self.ixk = []
        self.hkeys = {"xk": {}, "xki": {}}
        self.Nk = {128: 4, 192: 6, 256: 8}
        self.Nr = {128: 10, 192: 12, 256: 14}
        self.validate_key()

    @staticmethod
    def format_hkeys(xkb, Nr):
        """
        Formats the array of expanded key (xkb) or inverse expanded key (xki)
        in hexadecimal values and returns a dictionary with all round keys.

        :param: xkb: Array of the expanded AES key.
        :param: Nr: The numbers of rounds base on key length.
        :return: dkeys: Dictionary of formated round keys.
        """
        dkeys = {}
        for i in range(Nr + 1):
            kround = [xkb[4 * i], xkb[4 * i + 1], xkb[4 * i + 2], xkb[4 * i + 3]]
            kround = "0x" + "".join("{:08x}".format(x) for x in kround)
            dkeys[i] = kround
        return dkeys

    @staticmethod
    def rotw(w):
        """
        Simple rotate transformation to a 4-byte word.

        :param: w: 4-byte word.
        :return: 4-byte transformed word.
        """
        return w << 8 | w >> 24

    @staticmethod
    def subw(w):
        """
        Apply Sbox match to each byte in word w.

        :param: 4-byte word
        :return: 4-byte transformed word.
        """
        return (
            Sbox[w >> 24 & 0xFF] << 24
            | Sbox[w >> 16 & 0xFF] << 16
            | Sbox[w >> 8 & 0xFF] << 8
            | Sbox[w & 0xFF]
        )

    def validate_key(self):
        k = self.key

        base_len = {128, 192, 256}

        if not k.startswith("0x"):
            raise Exception(f'Wrong key format. Please consider this format: "0x{k}"')
            return

        k = k[2:]
        len_k = len(k) * 4
        if len_k not in {128, 192, 256}:
            raise Exception(f"Wrong key size! It should be {base_len}bits instead of {len_k}")
            return

        if not k.strip("0123456789abcdefABCDEF") == "":
            raise Exception("Wrong key format! It should be Hex.")

        self.key = k
        return True

    def expand_key(self):
        """
        Computes the expanded AES key given a 128, 192 or 256 bit key.
        :return:  Expanded AES Key. If `dec` is True, also returns the \n
                  decryption expanded AES Key in a tuple.
        """

        n = 8
        key = self.key
        len_xk = len(key)
        base = 4 * len_xk

        Nk, Nr = self.Nk[base], self.Nr[base]

        xkb = [0 for _ in range((Nr + 1) * 4)]
        output = [key[i : i + n] for i in range(0, len_xk, n)]

        for i in range(Nk):
            xkb[i] = int(output[i], 16)

        # Key expansion based on Golang implementation (https://golang.org/src/crypto/aes/block.go)
        for i in range(Nk, (4 * (Nr + 1))):
            t = xkb[i - 1]
            if i % Nk == 0:
                t = self.subw(self.rotw(t)) ^ (
                    powx[i // Nk - 1] << 24
                )  # It is equivalent to rcon[i//Nk-1]
            elif Nk > 6 and i % Nk == 4:
                t = self.subw(t)
            xkb[i] = xkb[i - Nk] ^ t

        # self.xk = xkb
        self.hkeys["xk"] = self.format_hkeys(xkb, Nr)

        if not self.dec:
            return xkb

        dec = [None for _ in range(len(xkb))]

        # Computes the decryption expanded keys from the encryption key
        for i in range(4):
            dec[i] = xkb[i]
            dec[((Nr + 1) - 1) * 4 + i] = xkb[((Nr + 1) - 1) * 4 + i]

        for i in range(4, ((Nr + 1) - 1) * 4):
            xb = xkb[i]
            t = (
                td0[Sbox[xb >> 24]]
                ^ td1[Sbox[xb >> 16 & 0xFF]]
                ^ td2[Sbox[xb >> 8 & 0xFF]]
                ^ td3[Sbox[xb & 0xFF]]
            )
            dec[i] = t

        # self.ixk = dec
        self.hkeys["xki"] = self.format_hkeys(dec, Nr)

        return (dec, xkb)

    def hexdump(self):
        pprint(self.hkeys)
