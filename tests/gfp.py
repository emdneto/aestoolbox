# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
#AES-128: Key size: 128 bits, Extended key size: 176 bytes, Nb of rounds: 10
from helpers.const import *

full1  = 0x46d5e16ec6f69fb1c4d1480a48228368
full2 = 0x46f64868c6d1836ec422e1b148d59f0a

expanded_key = "0x01010101020202020303030304040404f2f3f3f3f0f1f1f1f3f2f2f2f7f6f6f6b2b1b19b4240406ab1b2b2984644446eadaa2ec1efea6eab5e58dc33181c985d39ec626cd6060cc7885ed0f4904248a905beb10cd3b8bdcb5be66d3fcba425966c812113bf399cd8e4dff1e72f7bd4710dc98206b2f01ede562fef3979543b48ad2bd0b01fdbce6e49f4215730a01a1f568910b44952deda00a6ff8d3006e5920f505fb04602816a46a47ee776a29b75"
s = expanded_key[2:]
lenBytes = len(s)
lenK = int(len(s) / 8)
nr = int(lenK / 4)
#dec = [None for _ in range(lenBytes)]
#print(dec)

n=8
output = [s[i:i+n] for i in range(0, len(s), n)]
print(len(output))

dec = [None for _ in range(len(output))]

for i in range(4):
    dec[i] = output[i]
    dec[(nr-1)*4+i] = output[(nr-1)*4+i]

print(dec)


for i in range(4, (nr-1)*4):
    ab = int(output[i], 16)
    print(ab)
    t = td0[Sbox[ab>>24]] ^ td1[Sbox[ab>>16&0xff]] ^ td2[Sbox[ab>>8&0xff]] ^ td3[Sbox[ab&0xff]]
    dec[i] = hex(t)

print(dec)

s0 = 0x46f64868
s1 = 0xc6d1836e
s2 = 0xc422e1b1
s3 = 0x48d59f0a

for i in range(9,0, -1):
    k1 = int(dec[4*i], 16)
    k2 = int(dec[4*i+1], 16)
    k3 = int(dec[4*i+2], 16)
    k4 = int(dec[4*i+3], 16)
    print(hex(k1), hex(k2), hex(k3), hex(k4))
    tmp0 = td0[(s0>>24)] ^ td1[(s3>>16&0xff)] ^ td2[(s2>>8&0xff)] ^ td3[(s1&0xff)] ^ k1
    tmp1 = td0[s1>>24] ^ td1[s0>>16&0xff] ^ td2[s3>>8&0xff]  ^ td3[s2&0xff] ^ k2
    tmp2 = td0[s2>>24] ^ td1[s1>>16&0xff] ^ td2[s0>>8&0xff] ^ td3[s3&0xff] ^ k3
    tmp3 = td0[s3>>24] ^ td1[s2>>16&0xff] ^ td2[s1>>8&0xff] ^ td3[s0&0xff] ^ k4
    #print(hex(tmp0), hex(tmp1), hex(tmp2), hex(tmp3))
    s0, s1, s2, s3 = tmp0, tmp1, tmp2, tmp3


tmp0 = Sbox1[(s0>>24)] << 24 | Sbox1[(s3>>16&0xff)] <<16 | Sbox1[(s2>>8&0xff)] <<8 | Sbox1[(s1&0xff)] ^ int(dec[0], 16)
tmp1 = Sbox1[(s1>>24)] << 24 | Sbox1[(s0>>16&0xff)] <<16 | Sbox1[(s3>>8&0xff)] <<8 | Sbox1[(s2&0xff)] ^ int(dec[1], 16)
tmp2 = Sbox1[(s2>>24)] << 24 | Sbox1[(s1>>16&0xff)] <<16 | Sbox1[(s0>>8&0xff)] <<8 | Sbox1[(s3&0xff)] ^ int(dec[2], 16)
tmp3 = Sbox1[(s3>>24)] << 24 | Sbox1[(s2>>16&0xff)] <<16 | Sbox1[(s1>>8&0xff)] <<8 | Sbox1[(s0&0xff)] ^ int(dec[3], 16)
s0, s1, s2, s3 = tmp0, tmp1, tmp2, tmp3
#print(hex(s0), hex(s1), hex(s2), hex(s3))
#tmp1 = td0[s1>>24] ^ td1[s0>>16&0xff] ^ td2[s3>>8&0xff]  ^ td3[s2&0xff] ^ k2#
#tmp2 = td0[s2>>24] ^ td1[s1>>16&0xff] ^ td2[s0>>8&0xff] ^ td3[s3&0xff] ^ k3
#tmp3 = td0[s3>>24] ^ td1[s2>>16&0xff] ^ td2[s1>>8&0xff] ^ td3[s0&0xff] ^ k4



#    Si = s[i*8:64]
#    Sii = s[64:96]
#    print(Si)
#    print(Sii)
    #Si = int(Si, 16)
    #print(Si)
    #Si = hex(Si)
    #t = td0[Sbox[Si]]
    #dec[i] = td0[Sbox[Si>>24]]
    #print(td1[Sbox[Si>>16&0xff]])
    #dec[i] = td0[t>>24] ^ td1[t>>16&0xff] ^ td2[t>>8&0xff] ^ td3[t&0xff]

#print(dec)
#print(len(expanded_key[2:]))
#s1 = 0x8e84b08c
#s2 = 0x88f72b2e
#s3 = 0xe492a465

#s0 = 0x49a617d8
#s1 = 0x80d30204
#s2 = 0x82869f56
#s3 = 0x3e77047f

#k1 = 0x568910b4
#k2 = 0x4952deda
#k3 = 0x00a6ff8d
#k4 = 0x3006e592

#tmp_b0 = gfp14[s0>>24] ^ gfp11[s0>>16&0xff] ^ gfp13[s0>>8&0xff] ^ gfp9[s0&0xff]
#tmp_b1 = gfp9[s0>>24] ^ gfp14[s0>>16&0xff] ^ gfp11[s0>>8&0xff] ^ gfp13[s0&0xff]
#tmp_b2 = gfp13[s0>>24] ^ gfp9[s0>>16&0xff] ^ gfp14[s0>>8&0xff] ^ gfp11[s0&0xff]
#tmp_b3 = gfp11[s0>>24] ^ gfp13[s0>>16&0xff] ^ gfp9[s0>>8&0xff] ^ gfp14[s0&0xff]

#print(hex(tmp_b0), hex(tmp_b1), hex(tmp_b2), hex(tmp_b3))

'''
bkp = '{'
i = 0
for item in gfp13:
    bkp += f' {i}:FN({hex(item)});'
    i+=1
bkp += '}'
print(bkp)
'''
#s0 = gfp14[0xCE]
#s1 = gfp11[0x3c]
#s2 = gfp13[0xf0]
#s3 = gfp9[0xf1]

#print(hex(s0), hex(s1), hex(s2), hex(s3))
#a = s0 ^ s1
#b = s2 ^ s3
#c = a ^ b
#print(hex(c))


#tmp0 = td0[(s0>>24)] ^ td1[(s3>>16&0xff)] ^ td2[(s2>>8&0xff)] ^ td3[(s1&0xff)] 
#tmp1 = td0[s1>>24] ^ td1[s0>>16&0xff] ^ td2[s3>>8&0xff]  td3[s2&0xff] 
#tmp2 = td0[s2>>24] ^ td1[s1>>16&0xff] ^ td2[s0>>8&0xff] ^ td3[s3&0xff] 
#tmp3 = td0[s3>>24] ^ td1[s2>>16&0xff] ^ td2[s1>>8&0xff] ^ td3[s0&0xff] 
#print(hex(tmp0), hex(tmp1), hex(tmp2), hex(tmp3))

   


