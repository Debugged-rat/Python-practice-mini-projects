#https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

squareDimensions = list(input('What are the dimensions of the square? '))
userInput = ''
userInputList = []

whichNumberOfSectionX = 0
sectionX = 0
sectionSumX = []

whichNumberOfSectionY = 0
sectionY = 0
sectionSumY = []

whichNumberOfSectionDiagonal = 0
sectionDiagonal = 0
sectionSumDiagonal = [0, 0]

for i in range(int(squareDimensions[0])):
    for l in range(int(squareDimensions[0])):
        userInput = input('Insert (' + str(l) + ', ' + str(i) + ') number here: ')
        userInputList.append(userInput)
    sectionSumX.append(0)
    sectionSumY.append(0)

while sectionX != int(squareDimensions[0]):
    while whichNumberOfSectionX != int(squareDimensions[0]):
        sectionSumX[sectionX] += int(userInputList[sectionX * int(squareDimensions[0]) + whichNumberOfSectionX])
        whichNumberOfSectionX += 1
    whichNumberOfSectionX = 0
    sectionX += 1
if sectionSumX.count(sectionSumX[0]) != int(squareDimensions[0]):
    horizontal_match = False
else:
    horizontal_match = True

while sectionY != int(squareDimensions[0]):
    while whichNumberOfSectionY != int(squareDimensions[0]):
        sectionSumY[sectionY] += int(userInputList[whichNumberOfSectionY * int(squareDimensions[0]) + sectionY])
        whichNumberOfSectionY += 1
    whichNumberOfSectionY = 0
    sectionY += 1
if sectionSumY.count(sectionSumY[0]) != int(squareDimensions[0]) or sectionSumX[0] != sectionSumY[0]:
    vertical_match = False
else:
    vertical_match = True

while sectionDiagonal != 2:
    if sectionDiagonal == 0:
        sectionSumDiagonal[sectionDiagonal] += int(userInputList[whichNumberOfSectionDiagonal * (int(squareDimensions[0]) + 1)])
        whichNumberOfSectionDiagonal += 1
        if whichNumberOfSectionDiagonal != int(squareDimensions[0]):
            pass
        elif whichNumberOfSectionDiagonal == int(squareDimensions[0]):
            sectionDiagonal = 1
            whichNumberOfSectionDiagonal = 0
    elif sectionDiagonal == 1:
        sectionSumDiagonal[sectionDiagonal] += int(userInputList[(whichNumberOfSectionDiagonal + 1) * (int(squareDimensions[0]) - 1)])
        whichNumberOfSectionDiagonal += 1
        if whichNumberOfSectionDiagonal != int(squareDimensions[0]):
            pass
        elif whichNumberOfSectionDiagonal == int(squareDimensions[0]):
            sectionDiagonal = 2
if sectionSumDiagonal.count(sectionSumDiagonal[0]) != 2 or sectionSumX[0] != sectionSumDiagonal[0]:
    diagonal_match = False
else:
    diagonal_match = True

if horizontal_match == True and vertical_match == True and diagonal_match == True:
    print('\nFinal: True')
else:
    print('\nFinal: False')