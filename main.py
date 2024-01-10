import random 

print('Powerbal Lottery by inventwithpython')

while True:
    print('Enter 4 different numbers from 1 to 89, with space between')
    print('each number. (for example: 5 17 23 42 50)')
    response = input('> ')

    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, seperated by spaces')
        continue

    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
        
    except ValueError:
            print('please enter number , like 27, 35, or 65.')
            continue
        
    for i in range(5):
            if not (1 <= numbers[i] <= 89):
                print('the number must be between 1 and 89')
                continue
        
    if len(set(numbers)) != 5:
            print('You must enter 5 different numbers')
            continue

    break

while True:
    print('Enter the powerball number from 1 to 26.')
    response = ('> ')

    try:
        powerball = int(response)
    except ValueError:
        print('please enter a number, like 3, 15, or 22.')
        continue

    if not(1 <= powerball <= 26):
        print('the powerball number must be between 1 and 26')
        continue

    break 

while True:
    print('How many times do you want to play?')
    response = input('>')

    try:
        numPlays = int(response)
    except ValueError:
       print('please enter a number, like 3, 15, or 2000.')
       continue

    if not (1 <= numPlays <= 10000):
        print('you can play between 10000 times.')
        continue

    break 

price = '$' + str(2 * numPlays):
print('It costs', price, 'to play', numPlays, 'times, but don\'t)
print('worry. I am sure you will win it back.')
input('press enter to start...')

possibleNumbers = list(range(1, 90))
for i in range(numPlays):
        random.shuffle(possibleNumbers)
        winningNumbers = possibleNumbers[0:5]
        winningPowerball = random.randint(1, 26)
    
    print('The winning number are:', end='')
    allWinningNums = ''
    for i in range(5)
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' str(winningPowerball)
    print(allWinningNums.ljust(21), end=' ')

    


