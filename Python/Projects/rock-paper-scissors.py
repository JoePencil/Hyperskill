"""this code have line lenght of 79 charecter"""

import random
from pprint import pprint

# option = (
#     'rock', 'gun', 'lighting', 'devil', 'dragon', 'water', 'air', 'paper',
#     'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'
# )

option = ('rock', 'paper', 'scissors')

def checkWin(user_choice: str, prog_choice: str, /) -> int:
    """
    return positive if program win
    return negative if user win
    return zero if draw
    """
    if user_choice in win_table[prog_choice]:
        return 1
    elif user_choice == prog_choice:
        return 0
    else:
        return -1


def getInput() -> str:
    while True:
        user_input = input()
        if user_input == '!exit':
            return ''
        elif user_input == '!rating':
            return '!rating'
        elif user_input not in user_option:
            print('Invalid input')
        elif user_input in user_option:
            return user_input


user_name = input('Enter your name: ')
user_score = 0
print('Hello,', user_name)
user_option = tuple(input().split(','))
if user_option == ('', ):
    user_option = option

win_table = {
    user_option[i]: tuple([user_option[j]
        for j in range(i, i - (len(user_option) - 1) // 2 - 1, -1)][1:]
    )
    for i in range(len(user_option))
}
print("Okay, let's start")

while True:
    # may cause file not found error
    with open('rating.txt', 'r') as f:
        lines = [i.strip().split() for i in f.readlines()]
        for name, score in lines:
            if name == user_name:
                user_score = score
                break

    user_input = getInput()
    if not user_input:
        break
    elif user_input == '!rating':
        print(f'Your rating: {user_score}')
        continue

    prog_choice = random.choice(user_option)

    game_state = checkWin(user_input, prog_choice)

    if game_state == 1:
        print(f'Sorry, but computer chose {prog_choice}')
    elif game_state == -1:
        print(f'Well done. Computer chose {prog_choice} and failed')
        user_score += 100
    elif game_state == 0:
        print(f'There is a draw ({user_input})')
        user_score += 50

print('Bye!')
