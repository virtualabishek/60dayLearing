from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# 16 bits i.e 128 bits
key = get_random_bytes(16) 
print("AES Key:", key.hex())


data = b"HelloAbi" 
print("Original Data:", data)

iv = get_random_bytes(16)


# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_data = pad(data, AES.block_size)
encrypted_data = cipher.encrypt(padded_data)
print("Encrypted Data:", encrypted_data.hex())

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_padded_data = decipher.decrypt(encrypted_data)
decrypted_data = unpad(decrypted_padded_data, AES.block_size)
print("Decrypted Data:", decrypted_data)
