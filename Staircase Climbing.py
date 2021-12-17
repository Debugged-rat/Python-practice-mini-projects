from itertools import product
import math

userInput = int(input("How many steps are there? "))

def climbStairs(n):
    x = 1
    for i in range(math.ceil(n/2), n):
        y = list(product([1, 2], repeat=i))
        x += len([z for z in y if sum(z) == n])
    return x
print("There are " + climbStairs(20) + " possible ways to climb the " + str(userInput) + " step staircase. ")