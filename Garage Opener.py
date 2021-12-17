#https://www.reddit.com/r/dailyprogrammer/comments/4cb7eh/20160328_challenge_260_easy_garage_door_opener/

userInput = ''
userInputList = []
possibleCommands = ['button_clicked', 'cycle_complete', 'block_detected', 'block_cleared']
displayedCommands = ['> Button clicked.', '> Cycle complete.', '> Block detected!', '> Block cleared']
doorStateIDs = ['CLOSED', 'CLOSING' , 'OPEN', 'OPENING', 'STOPPED_WHILE_CLOSING', 'STOPPED_WHILE_OPENING', 'EMERGENCY_OPENING', 'OPEN_BLOCKED']

while userInput != 'done':
    userInput = input('Input individual commands here: ')
    userInputList.append(userInput)

doorState = 0
blockedState = False

print('\nDoor: ' + doorStateIDs[doorState] + '\n')

while userInputList[0] != 'done':
    if blockedState == False:        
        if userInputList[0] == possibleCommands[0]:
            print(displayedCommands[0])
            if doorState == 0 or doorState == 4:
                doorState = 3
            elif doorState == 2 or doorState == 5:
                doorState = 1
            elif doorState == 1:
                doorState = 4
            elif doorState == 3:
                doorState = 5
        elif userInputList[0] == possibleCommands[1]:
            print(displayedCommands[1])
            if doorState == 1:
                doorState = 0
            elif doorState == 3:
                doorState = 2
        elif userInputList[0] == possibleCommands[2]:
            print(displayedCommands[2])
            blockedState = True
            if doorState == 1:
                doorState = 6
    elif blockedState == True:
        if userInputList[0] == possibleCommands[3]:
            print(displayedCommands[3])
            blockedState = False
            if doorState == 6:
                doorState = 3
            elif doorState == 7:
                doorState = 2
        elif userInputList[0] == possibleCommands[1] and doorState == 6:
            print(displayedCommands[1])
            doorState = 7
        elif userInputList[0] == possibleCommands[0]:
            print(displayedCommands[0])
        elif userInputList[0] == possibleCommands[2]:
            print(displayedCommands[2])
    userInputList.remove(userInputList[0])
    print('Door: ' + doorStateIDs[doorState] + '\n')