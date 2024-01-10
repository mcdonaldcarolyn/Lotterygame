import random 

print('Powerbal Lottery by inventwithpython')

While True:
    print('Enter 4 different numbers from 1 to 89, with space between')
    print('each number. (for example: 5 17 23 42 50)')
    response = input('> ')

    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, seperated by spaces')