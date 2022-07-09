# Determining the mean of three Numbers
# Algorith
# 1. Ask the user of his or her three numbers
# 2. Do the math
# 3. Print to the user

firstNum = int(input('Enter your first digit: '))
secondNum = int(input('Enter your second digit: '))
thirdNum = int(input('Enter your third digit: '))

def medianFunction(firstNum, secondNum, thirdNum):
    medianList = []
    medianList.append(firstNum)
    medianList.append(secondNum)
    medianList.append(thirdNum)
    medianList.sort()
    return medianList[1]

medianValue = medianFunction(firstNum, secondNum, thirdNum)
print(medianValue)


    