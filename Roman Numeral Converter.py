#https://www.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

romanNumeralList = ["I", "V", "X", "L", "C", "D", "M"]
numbersList = [1, 5, 10, 50, 100, 500, 1000]
numbersDigitsList = [[1, 5, 10], [10, 50, 100], [100, 500, 1000], [1000]]
numberSystemsList = ["roman numeral", "number"]

def romanNumeralConvert(userInput):
    userInputRomanNumeralIndex = []
    singleDigitsCombinedList = []
    doubleDigitsIndexList = []
    doubleDigitsCombinedList = []
    convertedValue = 0
    for x in userInput:
        userInputRomanNumeralIndex.append(romanNumeralList.index(x))
    singleDigitsIndexList = userInputRomanNumeralIndex.copy()
    for x in range(len(userInputRomanNumeralIndex)):
        if x > 0:
            if userInputRomanNumeralIndex[x - 1] < userInputRomanNumeralIndex[x]:
                doubleDigitsIndexList.insert(0, [x - 1, x])
    for x in doubleDigitsIndexList:
        singleDigitsIndexList.pop(x[1])
        singleDigitsIndexList.pop(x[0])
        doubleDigitsCombinedList.append(numbersList[userInputRomanNumeralIndex[x[1]]] - numbersList[userInputRomanNumeralIndex[x[0]]])
    for x in singleDigitsIndexList:
        singleDigitsCombinedList.append(numbersList[x])
    singleDigitsCombinedList.extend(doubleDigitsCombinedList)
    for x in singleDigitsCombinedList:
        convertedValue += x
    return str(convertedValue)

def numberConvert(userInput):
    finalRomanNumeralList = []
    userInputList = list(userInput)
    for x in range(len(userInputList)):
        userInputList[x] = int(userInputList[x])
    for x in range(len(userInputList) - 1, -1, -1):
        addedRomanNumeral = []
        whichRomanNumeralIndex = (len(userInputList) - 1) - x
        if userInputList[x] >= 1 and userInputList[x] <= 3:
            for i in range(userInputList[x]):
                addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][0])])
        elif userInputList[x] == 4:
            addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][0])])
            addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][1])])
        elif userInputList[x] >= 5 and userInputList[x] <= 8:
            addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][1])])
            for i in range(userInputList[x] - 5):
                addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][0])])
        elif userInputList[x] == 9:
            addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][0])])
            addedRomanNumeral.append(romanNumeralList[numbersList.index(numbersDigitsList[whichRomanNumeralIndex][2])])

        finalRomanNumeralList.insert(0, "".join(addedRomanNumeral))
    convertedValue = "".join(finalRomanNumeralList)
    return convertedValue

conversionType = int(input("\nType \"1\" for roman numerals to numbers; Type \"2\" for numbers to roman numerals: " ))
userInput = input("\nInput your " + numberSystemsList[conversionType - 1] + " here: ")

if conversionType == 1:
    print("\nThe Roman Numeral \'" + userInput + "\' converts to " + romanNumeralConvert(userInput) + " in the Hindu-Arabic Number System.")
elif conversionType == 2:
    print("\nThe number " + userInput + " converts to " + numberConvert(userInput) + " in Roman Numerals.")
