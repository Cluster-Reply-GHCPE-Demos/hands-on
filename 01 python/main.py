# write rock paper scissors game

import random

def play():
    choices = ['r', 'p', 's', 'l', 'sp']

    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard, 'sp' for Spock\n")

    # user input validation
    if user not in choices:
        return 'Invalid input'

    computer = random.choice(choices)

    print(f'Computer chose {computer}')

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    win_map = {
        'r': ['s', 'l'],
        'p': ['r', 'sp'],
        's': ['p', 'l'],
        'l': ['p', 'sp'],
        'sp': ['r', 's']
    }
    return opponent in win_map.get(player, [])

if __name__ == '__main__':
    print(play())