import base64

# Encrypted data (change this to your actual encrypted data)
encrypted_data = base64.b64decode("BJoU5ozLBotcH/CkmLIRPqHVXDQXecq6ZJUus3vE9F7GAA==")

# Assuming the key used for encryption is 'Key' (adjust this to match your actual key)
key = 'Key'

# Convert the key to bytes (if it's not already in bytes)
key_bytes = [57, 150, 180, 192, 169, 13, 50, 132, 61, 108, 50, 35, 123, 68, 107, 62, 141, 19, 39, 25, 56, 180, 124, 34, 2, 44, 160, 4, 140, 147, 109, 32]

# Perform XOR decryption
decrypted = bytes([encrypted_byte ^ key_byte for encrypted_byte, key_byte in zip(encrypted_data, key_bytes)])

# Print the decrypted data
print("Decrypted data:", decrypted)
