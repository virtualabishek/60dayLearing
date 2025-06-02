import hashlib

def generateMD5Hash(inputText):
    return hashlib.md5(inputText.encode()).hexdigest()

def generateSHA1Hash(inputText):
    return hashlib.sha1(inputText.encode()).hexdigest()

def generateSHA256Hash(inputText):
    return hashlib.sha256(inputText.encode()).hexdigest()

def runHashingDemo():
    inputTexts = ["HelloAbi", "securePassword", "Nepal2025", "BITChitwan", "hashMe"]

    for text in inputTexts:
        md5Hash = generateMD5Hash(text)
        sha1Hash = generateSHA1Hash(text)
        sha256Hash = generateSHA256Hash(text)
        

        print(f"Text: {text}")
        print(f"  MD5     : {md5Hash}")
        print(f"  SHA-1   : {sha1Hash}")
        print(f"  SHA-256 : {sha256Hash}")
        print("")


runHashingDemo()
