#https://www.reddit.com/r/dailyprogrammer/comments/5j6ggm/20161219_challenge_296_easy_the_twelve_days_of/

giftsArchive = {
    '1': 'a Partridge in a Pear Tree',
    '2': 'two Turtle Doves',
    '3': 'three French Hens',
    '4': 'four Calling Birds',
    '5': 'five Golden Rings',
    '6': 'six Geese a Laying',
    '7': 'seven Swans a Swimming',
    '8': 'eight Maids a Milking',
    '9': 'nine Ladies Dancing',
    '10': 'ten Lords a Leaping',
    '11': 'eleven Pipers Piping',
    '12': 'twelve Drummers Drumming'
}
numberDay_of_Christmas = ["", "first","second","third","fourth", "fifth", 
"sixth","seventh","eighth","nineth","tenth","eleventh", 
"twelveth"]
whichDay = 1
whichPresent = 1
wordAnd = ''
for i in '123456789012':
    print('On the ' + numberDay_of_Christmas[whichDay] + ' day of Christmas,')
    print('my true love gave to me...\n')
    while whichPresent != 0:
        print(wordAnd + giftsArchive[str(whichPresent)])
        whichPresent -= 1
        wordAnd = ''
        if whichPresent == 1:
            wordAnd = 'and '        
    whichDay += 1
    whichPresent = whichDay
    print('\n')