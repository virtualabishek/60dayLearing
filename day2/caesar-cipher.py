def caesarEncryption(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result = result + chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result = result + chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result = result + char
    return result

def caesarDecryption(text, shift):
    return caesarEncryption(text, 26 - shift)

message = "Hello Tribhuwan University"
shift = 4

encrypted = caesarEncryption(message, shift)
decrypted = caesarDecryption(encrypted, shift)


print("Origibal is:", message)
print("Encrypted is:", encrypted)
print("Decrypted is:", decrypted)


