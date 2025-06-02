import bcrypt
import jwt
import datetime
import pyotp

def hashPassword(plainPassword):
    return bcrypt.hashpw(plainPassword.encode(), bcrypt.gensalt())

def verifyPassword(plainPassword, hashedPassword):
    return bcrypt.checkpw(plainPassword.encode(), hashedPassword)

def generateJWTToken(userId, secretKey):
    tokenData = {
        "userId": userId,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    }
    return jwt.encode(tokenData, secretKey, algorithm="HS256")

def verifyJWTToken(token, secretKey):
    try:
        return jwt.decode(token, secretKey, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None

def generateTOTPSecret():
    return pyotp.random_base32()

def getCurrentOTP(secretKey):
    return pyotp.TOTP(secretKey).now()

def verifyOTP(secretKey, otpInput):
    return pyotp.TOTP(secretKey).verify(otpInput)

def runAuthenticationSystem():
    userPassword = "HelloAbiSecure"
    secretKey = "SuperSecretKey123"

    hashedPassword = hashPassword(userPassword)
    isPasswordCorrect = verifyPassword("HelloAbiSecure", hashedPassword)

    if not isPasswordCorrect:
        print("Invalid Password")
        return

    jwtToken = generateJWTToken(userId=101, secretKey=secretKey)
    tokenPayload = verifyJWTToken(jwtToken, secretKey)

    if not tokenPayload:
        print("Token expired or invalid")
        return

    totpSecret = generateTOTPSecret()
    otpNow = getCurrentOTP(totpSecret)
    isOtpValid = verifyOTP(totpSecret, otpNow)

    print("Password Verified:", isPasswordCorrect)
    print("JWT Token:", jwtToken)
    print("Token Payload:", tokenPayload)
    print("Generated OTP:", otpNow)
    print("OTP Valid:", isOtpValid)


runAuthenticationSystem()
