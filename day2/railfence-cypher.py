def railFecnceEncryption(text, key):
    rail = ['' for _ in range(key)]
    direction_down = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)


def railFecnceDecryption(ciphertext, key):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*' and index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1
    return ''.join(result)


message = "HELLOTU"

encrypted = railFecnceEncryption(message, 3)
decrypted = railFecnceDecryption(encrypted, 3)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)