# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
import sys

def balanced(combination):
    listedCombination = list(combination)
    if listedCombination.count("x") == listedCombination.count("y"):
        return('True')
    else:
        return('False')

#bonus

def balanced_bonus(combination):
     listedCombination = list(combination)
     if listedCombination.count("x") == listedCombination.count("y"):
        if listedCombination.count("z") == listedCombination.count("x"):
            return('True')
        else:
            return('False')
     else:
        return('False')

bonus = input('Bonus? ')
userInput = input('Enter the value: ')
if bonus == 'yes':
    print(balanced_bonus(userInput))
else:
    print(balanced(userInput))

sys.exit()