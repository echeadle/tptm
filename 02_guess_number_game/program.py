import random
print('-' * 40)
print('        GUESS THAT NUMBER GAME')
print('-' * 40)
print()

the_number = random.randint(0,100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print(f'Sorry {name} your guess of {guess} is too low')
    elif guess > the_number:
        print('too high')
    else:
        print('you win!')

print('done')