#https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

import random

print('\nEnter your sequence of consanants and vowels as c\'s and v\'s.')

userInput = list(input('Enter sequence here: '))
sumOfLetters = userInput.count('c') + userInput.count('v') + userInput.count('C') + userInput.count('V')

while sumOfLetters != len(userInput):
    print('Error: Please only enter c\'s and v\'s as your input!')
    userInput = list(input('Re-enter letter pattern here: '))
    sumOfLetters = userInput.count('c') + userInput.count('v') + userInput.count('C') + userInput.count('V')

capitalUserInput = []
for letter in userInput:
    if letter.isupper() == True:
        capitalUserInput.append(True)
    elif letter.islower() == True:
        capitalUserInput.append(False)
        
userInput = ''.join(userInput)
userInput = userInput.lower()
userInput = list(userInput)

wordCheckList = []
matchingWordsList = []

vowels = ['a', 'e', 'i', 'o', 'u']

wordList = open('/Users/henryyang/Documents/Coding/Referencing/AllWords.txt', 'r')

for word in wordList:
    word = list(word)
    word.remove('\n')
    word = ''.join(word)
    for letter in word:
        try:
            vowels.index(letter.lower())
        except:
            wordCheckList.append('c')
        else:
            wordCheckList.append('v')
    if wordCheckList == userInput:
        matchingWordsList.append(word)
    wordCheckList.clear()

try:
    finalWord = list(random.choice(matchingWordsList))
except:
    print('Error: There aren\'t any english words that match that sequence of letters...')
else:
    fullList = input('Would you like to see all ' + str(len(matchingWordsList)) + ' words that match your sequence (if no, only one word from the list will be displayed.)? ')
    if fullList.lower() != 'yes':
        for i in range(len(userInput)):
            if capitalUserInput[i] == True:
                finalWord[i] = finalWord[i].upper()
            else:
                finalWord[i] = finalWord[i].lower()
        print(''.join(finalWord))
    else:
        for i in range(len(matchingWordsList)):
            print(matchingWordsList[i].lower())
wordList.close()