def computeGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def findMultiplicativeInverse(e, totient):
    t, newT = 0, 1
    r, newR = totient, e
    while newR != 0:
        quotient = r // newR
        t, newT = newT, t - quotient * newT
        r, newR = newR, r - quotient * newR
    return t + totient if t < 0 else t


def generateRSAKeys():
    prime1 = 61
    prime2 = 53
    modulus = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)

    publicExponent = 17
    privateExponent = findMultiplicativeInverse(publicExponent, totient)

    return (publicExponent, modulus), (privateExponent, modulus)


def encryptRSA(message, publicKey):
    exponent, modulus = publicKey
    return pow(message, exponent, modulus)


def decryptRSA(cipherText, privateKey):
    exponent, modulus = privateKey
    return pow(cipherText, exponent, modulus)


def runRSAEncryptionDemo():
    publicKey, privateKey = generateRSAKeys()

    message = 42
    cipherText = encryptRSA(message, publicKey)
    decryptedMessage = decryptRSA(cipherText, privateKey)

    print("Original Message:", message)
    print("Encrypted Message:", cipherText)
    print("Decrypted Message:", decryptedMessage)


runRSAEncryptionDemo()
