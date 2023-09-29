import json, base64


class N:
    @staticmethod
    def parse_n(n: str) -> int:
        buff = base64.b64decode(n)

        byte_arr = [b for b in buff]
        bytes_length = len(buff)
        cipher_text = "".join([chr(b) for b in buff])

        #print(
        #    f"""
        #\r[cyper-text] {cipher_text}
        #\r[n-bytes] {byte_arr[:50]}
        #\r[n-len] {len(n)}
        #\r[b64-bytes] {bytes_length}
        #"""
        #)

        return buff

'''
The Tiny Encryption Algorithm.
Simple and fast symmetric-key algorithm cipher.

Functions:
    tea_encrypt(), tea_decrypt() -- standard TEA encrypting.
    xtea_encrypt(), xtea_decrypt() -- extended TEA encrypting.
'''

from ctypes import c_uint32 as uint32
from struct import pack, unpack

def xtea_encrypt(plaintext, key):
    '''
    Encrypt a plaintext using XTEA algorithm.

    plaintext: 64 bits length bytes-like object.
    key: 128 bits length bytes-like object.

    Return a 64 bits length bytes object.
    '''

    v0, v1 = map(uint32, unpack('>2I', plaintext))
    k = tuple(map(uint32, unpack('>4I', key)))
    sm, delta = uint32(0), uint32(0x9E3779B9)

    for i in range(32):
        v0.value += (((v1.value << 4) ^ (v1.value >> 5)) + v1.value) ^ (sm.value + k[sm.value & 3].value)
        sm.value += delta.value
        v1.value += (((v0.value << 4) ^ (v0.value >> 5)) + v0.value) ^ (sm.value + k[(sm.value >> 11) & 3].value)

    return pack('>2I', v0.value, v1.value)


def xtea_decrypt(ciphertext, key):
    '''
    Decrypt a ciphertext using XTEA algorithm.

    ciphertext: 64 bits length bytes-like object.
    key: 128 bits length bytes-like object.

    Return a 64 bits length bytes object.
    '''

    v0, v1 = map(uint32, unpack('>2I', ciphertext))
    k = tuple(map(uint32, unpack('>4I', key)))
    sm, delta = uint32(0xC6EF3720), uint32(0x9E3779B9)

    for i in range(32):
        v1.value -= (((v0.value << 4) ^ (v0.value >> 5)) + v0.value) ^ (sm.value + k[(sm.value >> 11) & 3].value)
        sm.value -= delta.value
        v0.value -= (((v1.value << 4) ^ (v1.value >> 5)) + v1.value) ^ (sm.value + k[sm.value & 3].value)

    return pack('>2I', v0.value, v1.value)


data = N.parse_n('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')
print(xtea_decrypt(data, 'xx'))