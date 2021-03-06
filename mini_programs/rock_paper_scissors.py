### Created on 15-1-2019

from random import choice

# Determines whether the player wins, loses, or draws
def result(player_choice, comp_choice):
    if player_choice == comp_choice:
        print('Tie!!')
    elif player_choice == 'Rock':
        if comp_choice == 'Paper':
            print('You lose!\n', comp_choice, 'covers', player_choice)
        else:
            print('You win!\n', player_choice, 'smashes', comp_choice)
    elif player_choice == 'Paper':
        if comp_choice == 'Rock':
            print('You win!\n', player_choice, 'covers', comp_choice)
        else:
            print('You lose!\n', comp_choice, 'cut', player_choice)
    elif player_choice == 'Scissors':
        if comp_choice == 'Rock':
            print('You lose!\n', comp_choice, 'smashes', player_choice)
        else:
            print('You win!\n', player_choice, 'cut', comp_choice)


# Display the player choice, computer choice, & the result
def display_result(player_choice, comp_choice):
    print('\tComputer\'s choice:', comp_choice)
    print('\tYour choice:', player_choice)
    
    result(player_choice, comp_choice)


# List of play options
options = ['Rock', 'Paper', 'Scissors']

while True:
    computer = choice(options) # Pick rock, paper, or scissors randomly for the computer
    player = input(
        '\nRock, Paper, Scissors?\nChoose one (blank to quit): '
    ).capitalize()
    
    if player in options:
        display_result(player, computer)
    elif player == '':  # Stop the program
        break
    else:
        print('Invalid choice')
