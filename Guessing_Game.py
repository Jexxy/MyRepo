import random as rand
from os import system
from sys import platform

# Checks if system is linux or windows, and gives the correct clear function to cls()
if platform == "win32":
    cls = lambda: system('cls')
elif platform == "linux":
    cls = lambda: system('clear')


# This function will continue to loop forever until given usable input or told to exit.
def get_guess():
    while True:  # Use a while loop here so it will continue the program unless otherwise told, and will not crash.
        try:  # Get user's guess
            guess_num = int(input('''Please enter a number between 1-100 to make your guess: '''))
            cls()
        except ValueError:  # Catches the ValueError that happens when people don't put in a number
            while True:  # Starts a loop here so they HAVE to type Y or N, any other input simply wont work.
                try_again = input("You must enter a number! Try again? Y/n: ")
                if try_again.lower() == "y" or try_again.lower() == "n" or try_again == "":  # Making sure the input is Y or N
                    if try_again.lower() == "n":
                        exit(0)  # Exits the program with exit code 0
                    else:
                        break  # Breaking the nested while loop
            continue  # Continues to the next iteration of the loop. Otherwise it would just do the if statement.
        if 0 < guess_num < 100 and isinstance(guess_num, int):  # Checks if guess_num is between 1 and 100
            return guess_num
        else:
            while True:  # user enters y, n, or null to continue. Lets user know num anything outside 1-100 will error
                try_again = input("Your guess is not between 1-100! Do you want to try again? Y/n: ")
                if try_again.lower() == "y" or try_again.lower() == "n" or try_again == "":
                    if try_again.lower() == "n":
                        exit(0)
                    else:
                        break


def main():
    random_number = rand.randrange(1, 100)  # Generates the random number
    game_iteration = 1  # Keeps track of the game iteration
    previous_guesses = []  # Stores previous guess to display them later.
    while True:  # Firs thing the user sees, asks them if they are ready to play.
        cls()
        ready_to_start = input('''Welcome to the guessing game!
        A Random number between 1-100 has already been generated!
        Are you ready to start? Y/n: ''')
        cls()
        if ready_to_start.lower() == "y" or ready_to_start.lower() == "n" or ready_to_start == "":
            if ready_to_start.lower() == "n":
                exit(0)
            else:
                break
    while True:  # Win/Lose states + Higher lower states, as well as displays previous guesses.
        user_guess = get_guess()
        previous_guesses.append(user_guess)
        if game_iteration == 5:
            print(f"You have guessed five times! You lost! The random number was: {random_number}")
            break
        elif user_guess == random_number:
            print("Congrats! You have guessed correctly!")
            break
        elif user_guess < random_number:
            print("Your guess was lower than the random number.")
            print(f"Your previous guesses were: {previous_guesses}")
        elif user_guess > random_number:
            print("Your guess was higher than the random number.")
            print(f"Your previous guesses were: {previous_guesses}")
        if game_iteration == 5:
            play_again = input("Would you like to play again? Y/n: ")  # Checking to see if they want to play again.
            if play_again.lower() == "y" or play_again == "":
                continue
            else:
                exit(0)
        game_iteration += 1


main()
