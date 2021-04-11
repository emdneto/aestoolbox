====
AES-Toolbox
====


.. image:: https://img.shields.io/pypi/v/aestoolbox.svg
        :target: https://pypi.python.org/emdneto/aestoolbox

.. image:: https://img.shields.io/travis/latarc/aestoolbox.svg
        :target: https://travis-ci.com/emdneto/aestoolbox

.. image:: https://readthedocs.org/projects/aestoolbox/badge/?version=latest
        :target: https://aestoolbox.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/latarc/aestoolbox/shield.svg
     :target: https://pyup.io/repos/github/latarc/aestoolbox/
     :alt: Updates


An AES Toolbox for computing Rijndael key schedule given a 128, 192, or 256-bit key.

* Documentation: https://aestoolbox.readthedocs.io.


Features
--------

* Encryption/Decryption Key Scheduling
* AES Encrypt/Decrypt (working in progress)

Get AES-Toolbox from source
-----------------------

First, clone the `AES-Toolbox GitHub repository <https://github.com/emdneto/aestoolbox>`_ using git:

.. code-block:: bash

    $ git clone https://github.com/emdneto/aestoolbox


* Free software: GNU General Public License v3
* Documentation: https://aestoolbox.readthedocs.io.


Usage (via CLI)
---------------

.. code-block:: bash

    $ aes-schedule [-h] [-v] [-i] key
    $ aes-schedule 0x0101010102020202030303030404040 -i -v

The above command should output:

.. code-block:: python

        {'xk': 
        {0: '0x01010101020202020303030304040404',
        1: '0xf2f3f3f3f0f1f1f1f3f2f2f2f7f6f6f6',
        2: '0xb2b1b19b4240406ab1b2b2984644446e',
        3: '0xadaa2ec1efea6eab5e58dc33181c985d',
        4: '0x39ec626cd6060cc7885ed0f4904248a9',
        5: '0x05beb10cd3b8bdcb5be66d3fcba42596',
        6: '0x6c812113bf399cd8e4dff1e72f7bd471',
        7: '0x0dc98206b2f01ede562fef3979543b48',
        8: '0xad2bd0b01fdbce6e49f4215730a01a1f',
        9: '0x568910b44952deda00a6ff8d3006e592',
        10: '0x0f505fb04602816a46a47ee776a29b75'},
        
        'xki': 
        {0: '0x01010101020202020303030304040404',
         1: '0xfdfafef8fff8fcfafcfbfff9f8fffbfd',
         2: '0xc263931b3d9b6fe1c1609018399f6be5',
         3: '0x70e738474d7c57a68c1cc7beb583ac5b',
         4: '0xa68450a9ebf8070f67e4c0b1d2676cea',
         5: '0xb86800d6539007d93474c768e613ab82',
         6: '0xffd917eeac491037983dd75f7e2e7cdd',
         7: '0xe238ed774e71fd40d64c2a1fa86256c2',
         8: '0xc20b68478c7a95075a36bf18f254e9da',
         9: '0x7edace11f2a05b16a896e40e5ac20dd4',
         10: '0x0f505fb04602816a46a47ee776a29b75'}}


Usage as Python Library
-----------------------

Soon




