# The guessing game will have the following requirements:
#
# Randomly generate a number between 1 and 100 (10 points)
# Not accept numbers less then 1 (5 points)
# Not accept numbers greater then 100 (5 points)
# Let the user know if the guess is to high or to low (5 points)
# Have a limit of 5 trys (5 points)
# Exit the game if the number is guessed with a 'you win' type remark (5 points)
# Exit the game if the number of trys goes over the limit with a 'you lose' type remark (5 points)
# Extra Credit:

# After the game, ask the user if they would like to play again (10 points)

import random


# This function will continue to loop forever until given usable input or told to exit.
def get_guess():
    while True:  # Use a while loop here so it will continue the program unless otherwise told, and will not crash.
        try:  # Get user's guess
            guess_num = int(input('''Please enter a number between 1-100 to make your guess: '''))
        except ValueError:  # Catches the ValueError that happens when people don't put in a number
            while True:  # Starts a loop here so they HAVE to type Y or N, any other input simply wont work.
                try_again = input("You must enter a number! Try again? Y/N: ")
                if try_again.lower() == "y" or try_again.lower() == "n":  # Making sure the input is Y or N
                    if try_again.lower() == "n":
                        exit(0)  # Exits the program with exit code 0
                    else:
                        break  # Breaking the nested while loop
            continue  # Continues to the next iteration of the loop. Otherwise it would just do the if statement.
        if 0 < guess_num < 100 and isinstance(guess_num, int):
            return guess_num
        else:
            while True:
                try_again = input("Your guess is not between 1-100! Do you want to try again? Y/N: ")
                if try_again.lower() == "y" or try_again.lower() == "n":
                    if try_again.lower() == "n":
                        exit(0)
                    else:
                        break


def main():
    game_iteration = 0
    while True:
        ready_to_start = input('''Welcome to the guessing game!
                         A Random number between 1-100 has already been generated!
                         When ready, please type "Y" to start: ''')
        if ready_to_start.lower() != "y":
            continue
        else:
            break
    while True:


    print(get_guess())


main()