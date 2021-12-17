inputFrom = int(input("Which number do you want to start at? "))
inputTo = int(input("Which number do you want to end at? "))
primesList = []

for x in range(inputFrom, inputTo + 1):
    prime = True
    for i in range(2, x - 1):
        if x % i == 0:
            prime = False
            break
    if prime == True:
        primesList.append(str(x))

print("The prime numbers in the range of " + str(inputFrom) + " to " + str(inputTo) + " are:\n" + ", ".join(primesList))