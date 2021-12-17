#https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

userInput = input('Insert time here: ')
timeElements = list(userInput)
timeElements.remove(':')
if len(timeElements) == 3:
    timeElements.insert(0, '0')

ones = ["", "one","two","three","four", "five", 
"six","seven","eight","nine","ten","eleven", 
"twelve", "thirteen", "fourteen", "fifteen", 
"sixteen","seventeen", "eighteen","nineteen"]

tens = ["","","twenty","thirty","forty", "fifty"]

hours = int(timeElements[0] + timeElements[1])

if int(timeElements[0]) == 1 and int(timeElements[1]) >= 2:
    pm = ' PM'
    if int(timeElements[1]) >= 3:
                hours = hours - 12
elif int(timeElements[0]) == 2:
    pm = ' PM'
    hours = hours - 12
else:
    pm = ' AM'

displayedHours = ones[hours]

displayedMinutes1 = ''
displayedMinutes2 = ''

oh = ''
thingy = '-'

if timeElements[3] == '0' or timeElements[2] == '1':
    thingy = ''

if int(timeElements[2]) < 2:
    if int(timeElements[2]) == 0 and int(timeElements[3]) != 0:
        oh = 'oh'
        displayedMinutes1 = ones[int(timeElements[3])]
    elif int(timeElements[2]) == 0 and int(timeElements[3]) == 0:
        thingy = ''
    else:
        displayedMinutes1 = ones[int(timeElements[2] + timeElements[3])]
else:
    displayedMinutes1 = tens[int(timeElements[2])]
    displayedMinutes2 = ones[int(timeElements[3])]

print('Its ' + displayedHours + ' ' + oh + displayedMinutes1 + thingy + displayedMinutes2 + pm)