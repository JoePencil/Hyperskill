import random
from string import ascii_lowercase

WORD_LIST = 'python', 'java', 'kotlin', 'javascript'
answer = random.choice(WORD_LIST)

lives = 8

good_guessed, bad_guessed = str(), str()

print('\nH A N G M A N')

# game loop
while True:
    command = ''
    while command != 'play':
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == 'exit':
            exit()

    while lives and set(good_guessed) != set(answer):

        print()
        for c in answer:
            if c not in good_guessed:
                print('-', end='')
            else:
                print(c, end='')
        print()

        guessing = input("Input a letter: ")

        # bad input
        if len(guessing) != 1:
            print('You should input a single letter')
        elif guessing not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        # bad guessing
        elif guessing in good_guessed or guessing in bad_guessed:
            print('You already typed this letter')
        elif guessing not in answer:
            print('No such letter in the word')
            bad_guessed += guessing
            lives -= 1
        # good guess
        else:
            good_guessed += guessing

    if not lives:
        print('You are hanged!')
    else:
        print(f'\n{answer}')
        print('You guessed the word!')
        print('You survived!\n')