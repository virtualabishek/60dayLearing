from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

key = get_random_bytes(8)  
print("DES Key:", key.hex())

# Message to encrypt
data = b"HelloAbi"  
print("Original Data:", data)

# DES Encryption
cipher = DES.new(key, DES.MODE_ECB)
padded_data = pad(data, DES.block_size) 
encrypted_data = cipher.encrypt(padded_data)
print("Encrypted Data:", encrypted_data.hex())


# DES Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted_padded_data = decipher.decrypt(encrypted_data)
decrypted_data = unpad(decrypted_padded_data, DES.block_size)
print("Decrypted Data:", decrypted_data)
