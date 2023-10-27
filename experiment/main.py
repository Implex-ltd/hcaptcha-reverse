"""
xxxxxxxxxxxxxxXXxXx
1411266999
"""

import hashlib

print(int.from_bytes(hashlib.sha384(b"xxxxxxxxxxxxxxXXxXx").digest()[:4], 'little')) # 32-bit
#print(int.from_bytes(hashlib.sha512(b"xxxxxxxxxxxxxxXXxXx").digest()[:8], 'little')) # 64-bit