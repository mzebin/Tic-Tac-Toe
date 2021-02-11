# Importing Required Libraries
import copy
import os
import platform
import random
import time


# The Singleplayer Class
# It handles Single Player Game.
class SinglePlayer:
    pass


class Easy(SinglePlayer):
    pass


class Medium(SinglePlayer):
    pass


class Impossible(SinglePlayer):
    pass


# The Multiplayer Class
# It handles multiplayer game.
class MultiPlayer:
    pass


# The Board Class
# THis class has all methods
# associated with the board
class Board:
    pass


# Clear Screen
# This function clears the screen
# based on their os.
def clear_screen():
    # Checking platform and
    # Clearing Screen
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    # Printing Title
    print("Tic Tac Toe")
    print()


# Get Number of Players
# This function returns the number of
# players. (Single Player or MultiPlayer)
def get_num_players():
    try:
        # Getting number of players
        num_players = int(input("Singleplayer or Multiplayer (1 or 2) > "))

        # if number of players is valid
        # then return it else raise ValueError.
        if 0 < num_players < 3:
            return num_players
        else:
            raise ValueError
    except ValueError:
        # Asking if user wants to exit.
        ask_exit()
        return get_num_players()


def choose_difficulty_level():
    try:
        # Display Levels
        print("Levels")
        print("1. Easy")
        print("2. Medium")
        print("3. Impossible")

        # Choosing Level
        level = int(input("Choose Level (1, 2, or 3) > "))

        if 0 < level < 4:
            return level
        else:
            raise ValueError
    except ValueError:
        # Asking if user wants to exit.
        ask_exit()
        return choose_difficulty_level()


# Ask Exit function.
# This function asks user if he
# wants to exit.
def ask_exit():
    # Asking if user wants to exit.
    print()
    exit = input("type 'x' to exit > ")

    # if user wants to exit then exit else continue.
    if exit.lower() == "x":
        quit()
    else:
        print("You typed wrong...")
        time.sleep(3)
        clear_screen()


# Main Function
# This functions runs the game.
def main():
    running = True
    while running:
        # Clear Screen
        clear_screen()

        # Getting the number of players
        num_players = get_num_players()

        if num_players == 1:
            level = choose_difficulty_level()

            if level == 1:
                game = Easy()
                game.run()
            elif level == 2:
                game = Medium()
                game.run()
            elif level == 3:
                game = Impossible()
                game.run()
        else:
            game = MultiPlayer()
            game.run()

        # Asking if the player wants to play again.
        again = input("Do you want to play again? > ").lower()
        if not again.startswith("y"):
            break


# Starting the game.
if __name__ == "__main__":
    main()
