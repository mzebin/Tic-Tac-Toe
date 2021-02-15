# Importing Required Libraries
import copy
import os
import platform
import time

import numpy as np
from numpy import random


# The Single Player Class
# It handles Single Player Game.
class SinglePlayer:

    # Constructor
    def __init__(self):
        self.board = Board()
        self.player = "X"
        self.opponent = "O"
        self.game_over = False
        self.turn = random.choice([0, 1])

    # Getting Player Move
    def get_player_move(self):
        pass

    # MainLoop
    def run(self):
        pass


class Easy(SinglePlayer):

    # Constructor
    def __init__(self):
        super().__init__()


class Medium(SinglePlayer):

    # Constructor
    def __init__(self):
        super().__init__()


class Impossible(SinglePlayer):

    # Constructor
    def __init__(self):
        super().__init__()


# The Multiplayer Class
# It handles multiplayer game.
class MultiPlayer:

    # Constructor
    def __init__(self):
        pass

    def run(self):
        pass


# The Board Class
# This class has all methods
# associated with the board
class Board:

    # Constructor
    def __init__(self):
        self.size = 3
        self.filler = "_"
        self.board = self.make_board()

    # Checking for Win
    def is_winner(self, mark):
        # Checking Vertically for win
        for col in range(self.size):
            for row in range(self.size):
                if self.board[row, col] != mark:
                    break

                if row == self.size - 1:
                    return True

        # Checking Horizontally for win
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] != mark:
                    break

                if col == self.size - 1:
                    return True

        # Checking Diagonals for win
        for idx in range(self.size):
            if self.board[idx, idx] != mark:
                break

            if idx == self.size - 1:
                return True

        # Checking Diagonals for win
        col = self.size
        for row in range(self.size):
            col -= 1
            if self.board[row, col] != mark:
                break

            if row == self.size - 1:
                return True

    # Checking for Tie
    def is_tie(self):
        return len(self.get_available_moves()) == 0

    # Checking if a space is free.
    def is_free(self, row, col):
        return self.board[row, col] == self.filler

    # Making Move
    def make_move(self, row, col, mark):
        self.board[row, col] = mark

    # Undoing Move
    def undo_move(self):
        self.board[row, col] = self.filler

    # Returns the available moves
    def get_available_moves(self):
        available_moves = []
        for row, rows in self.board:
            for col, cell in enumerate(rows):
                if cell == self.filler:
                    available_moves.append((row, col))

        return available_moves

    # Making Board
    def make_board(self):
        board = np.zeros((self.size, self.size), dtype=int)
        board = np.where(board == 0, self.filler, board)
        return board

    # Returns a copy of the board.
    def copy(self):
        board = Board()
        board.board = copy.deepcopy(self.board)
        return board

    # Printing Board.
    def print_board(self):
        for row in self.board:
            print("+-----" * self.size + "+")
            for cell in row:
                print(f"|  {cell}  ", end="")
            print("|")
        print("+-----" * self.size + "+")


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
        num_players = int(input("Single Player or Multiplayer (1 or 2) > "))

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
    response = input("type 'x' to exit > ")

    # if user wants to exit then exit else continue.
    if response.lower() == "x":
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
    board = Board()
    board.print_board()
    board.make_move(0, 2, "x")
    board.make_move(1, 1, "x")
    board.make_move(2, 0, "x")
    if board.is_winner("x"):
        board.print_board()
        print("X won...")

    # main()
