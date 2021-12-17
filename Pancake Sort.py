#https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/

import random

def flipFront(n, array):
    flippedArray = array[:n]
    flippedArray = flippedArray[::-1]
    array[:n] = flippedArray

def pancakeSort(array):
    sortedCounter = 0
    while sortedCounter < len(array):
        whichSortedValue = (len(array) - 1) - sortedCounter
        if array[whichSortedValue] != max(array[:whichSortedValue + 1]):
            print(array)
            if array[0] != max(array[:whichSortedValue + 1]):
                flipFront(array.index(max(array[:whichSortedValue + 1])) + 1, array)
            else:
                flipFront(whichSortedValue + 1, array)
        else:
            sortedCounter += 1
        
exampleArray = []
for i in range(20):
    exampleArray.append(random.randint(1, 1000))
pancakeSort(exampleArray)
print(exampleArray)