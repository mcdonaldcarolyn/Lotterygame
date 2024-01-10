import random 

print('Powerbal Lottery by inventwithpython')

While True:
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
            if not (1 <= number[i] <= 89):
                print('the number must be between 1 and 89')
                continue
        
        if len(set(numbers)) != 5:
            print('You must enter 5 different numbers')
            continue

        break
        