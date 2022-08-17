import random


number = random.randint(1, 10)

while True:
    guess = int(input('Try to guess the number between 1 and 10: '))

    if guess > number:
        print('Too high. Try again!')
    elif guess < number:
        print('Too low. Try again!')
    else:
        print(f'You win! It was: {guess}')
        break
