def calculatePowerMod(base, exponent, modulus):
    return pow(base, exponent, modulus)


def runDiffieHellmanKeyExchange():
    primeModulus = 23
    primitiveRoot = 5

    privateKeyRam = 6
    privateKeyHari = 15

    publicKeyRam = calculatePowerMod(primitiveRoot, privateKeyRam, primeModulus)
    publicKeyHari = calculatePowerMod(primitiveRoot, privateKeyHari, primeModulus)

    sharedKeyRam = calculatePowerMod(publicKeyHari, privateKeyRam, primeModulus)
    sharedKeyHari = calculatePowerMod(publicKeyRam, privateKeyHari, primeModulus)

    print("Ram's Shared Key:", sharedKeyRam)
    print("Hari's Shared Key:", sharedKeyHari)


runDiffieHellmanKeyExchange()
