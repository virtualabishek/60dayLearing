def findGCDUsingEuclideanAlgorithm(firstNumber, secondNumber):
    while secondNumber != 0:
        remainder = firstNumber % secondNumber
        firstNumber = secondNumber
        secondNumber = remainder
    return firstNumber


def testEuclideanAlgorithm():
    numberPairs = [(48, 18), (101, 103), (56, 98), (270, 192), (75, 120)]

    for pair in numberPairs:
        firstNumber, secondNumber = pair
        gcd = findGCDUsingEuclideanAlgorithm(firstNumber, secondNumber)
        print(f"GCD of {firstNumber} and {secondNumber} is {gcd}")


testEuclideanAlgorithm()
