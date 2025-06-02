def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2  
    return True

def testPrimes():
    numbersToTest = [1, 2, 3, 4, 13, 25, 97, 100, 131]    
    for number in numbersToTest:
        if isPrime(number):
            print(f"{number} is a Prime number")
        else:
            print(f"{number} is NOT a Prime number ")
testPrimes()
