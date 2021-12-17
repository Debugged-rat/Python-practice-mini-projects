#https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/

number_of_entries = int(input('How many lines are there? '))
userInput = ''
masterKeyList = []
checkLetters = 0
maxWord = ''
maxWordLength = 0

for i in range(number_of_entries):
    userInput = list(input('Enter the lines here: '))
    masterKeyList.append(userInput)
print('')

for i in range(number_of_entries):
    wordList = open('/Users/henryyang/Documents/Coding/Referencing/AllWords.txt', 'r')
    for word in wordList:
        word = list(word)
        word.remove('\n')
        word = ''.join(word)
        for letter in word:
            try:
                masterKeyList[i].index(letter.lower())
            except:
                checkLetters += 1
        if checkLetters == 0:
            if len(word) > maxWordLength:
                maxWord = word
                maxWordLength = len(maxWord)
        else:
            checkLetters = 0
    if maxWord == '':
        maxWord = 'Error: there are no words that can be written with only those letters...'
    print(''.join(masterKeyList[i]) + ' = ' + maxWord)
    maxWord = ''
    maxWordLength = 0
    wordList.close()