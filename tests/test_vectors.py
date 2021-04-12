# Test vectors from https://www.samiam.org/key-schedule.html

test_vectors_128 = [
    {
        "key": "0x01010101020202020303030304040404",
        "round_keys": [
            0x01010101020202020303030304040404,
            0xF2F3F3F3F0F1F1F1F3F2F2F2F7F6F6F6,
            0xB2B1B19B4240406AB1B2B2984644446E,
            0xADAA2EC1EFEA6EAB5E58DC33181C985D,
            0x39EC626CD6060CC7885ED0F4904248A9,
            0x05BEB10CD3B8BDCB5BE66D3FCBA42596,
            0x6C812113BF399CD8E4DFF1E72F7BD471,
            0x0DC98206B2F01EDE562FEF3979543B48,
            0xAD2BD0B01FDBCE6E49F4215730A01A1F,
            0x568910B44952DEDA00A6FF8D3006E592,
            0x0F505FB04602816A46A47EE776A29B75,
        ],
    },
    {
        "key": "0x000102030405060708090a0b0c0d0e0f",
        "round_keys": [
            0x000102030405060708090A0B0C0D0E0F,
            0xD6AA74FDD2AF72FADAA678F1D6AB76FE,
            0xB692CF0B643DBDF1BE9BC5006830B3FE,
            0xB6FF744ED2C2C9BF6C590CBF0469BF41,
            0x47F7F7BC95353E03F96C32BCFD058DFD,
            0x3CAAA3E8A99F9DEB50F3AF57ADF622AA,
            0x5E390F7DF7A69296A7553DC10AA31F6B,
            0x14F9701AE35FE28C440ADF4D4EA9C026,
            0x47438735A41C65B9E016BAF4AEBF7AD2,
            0x549932D1F08557681093ED9CBE2C974E,
            0x13111D7FE3944A17F307A78B4D2B30C5,
        ],
    },
    {
        "key": "0x00000000000000000000000000000000",
        "round_keys": [
            0x00000000000000000000000000000000,
            0x62636363626363636263636362636363,
            0x9B9898C9F9FBFBAA9B9898C9F9FBFBAA,
            0x90973450696CCFFAF2F457330B0FAC99,
            0xEE06DA7B876A1581759E42B27E91EE2B,
            0x7F2E2B88F8443E098DDA7CBBF34B9290,
            0xEC614B851425758C99FF09376AB49BA7,
            0x217517873550620BACAF6B3CC61BF09B,
            0x0EF903333BA9613897060A04511DFA9F,
            0xB1D4D8E28A7DB9DA1D7BB3DE4C664941,
            0xB4EF5BCB3E92E21123E951CF6F8F188E,
        ],
    },
    {
        "key": "0xffffffffffffffffffffffffffffffff",
        "round_keys": [
            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
            0xE8E9E9E917161616E8E9E9E917161616,
            0xADAEAE19BAB8B80F525151E6454747F0,
            0x090E2277B3B69A78E1E7CB9EA4A08C6E,
            0xE16ABD3E52DC2746B33BECD8179B60B6,
            0xE5BAF3CEB766D488045D385013C658E6,
            0x71D07DB3C6B6A93BC2EB916BD12DC98D,
            0xE90D208D2FBB89B6ED5018DD3C7DD150,
            0x96337366B988FAD054D8E20D68A5335D,
            0x8BF03F233278C5F366A027FE0E0514A3,
            0xD60A3588E472F07B82D2D7858CD7C326,
        ],
    },
    {
        "key": "0x000102030405060708090a0b0c0d0e0f",
        "round_keys": [
            0x000102030405060708090A0B0C0D0E0F,
            0xD6AA74FDD2AF72FADAA678F1D6AB76FE,
            0xB692CF0B643DBDF1BE9BC5006830B3FE,
            0xB6FF744ED2C2C9BF6C590CBF0469BF41,
            0x47F7F7BC95353E03F96C32BCFD058DFD,
            0x3CAAA3E8A99F9DEB50F3AF57ADF622AA,
            0x5E390F7DF7A69296A7553DC10AA31F6B,
            0x14F9701AE35FE28C440ADF4D4EA9C026,
            0x47438735A41C65B9E016BAF4AEBF7AD2,
            0x549932D1F08557681093ED9CBE2C974E,
            0x13111D7FE3944A17F307A78B4D2B30C5,
        ],
    },
]