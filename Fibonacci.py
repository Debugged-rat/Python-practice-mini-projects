userInput = int(input('How many instances of the Fibonacci Sequence do you want displayed? '))
numberList = []
firstTwoNumbers = [0, 1]
numberList.append(str(firstTwoNumbers[1]))
for i in range(userInput - 1):
    numberTwo = firstTwoNumbers[0] + firstTwoNumbers[1]
    numberList.append(str(numberTwo))
    firstTwoNumbers[0] = firstTwoNumbers[1]
    firstTwoNumbers[1] = numberTwo
print(', '.join(numberList))
