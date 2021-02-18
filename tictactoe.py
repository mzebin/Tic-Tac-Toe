# Importing Required Libraries
import os
import platform
import random
import time
from copy import deepcopy

import numpy as np


# The Single Player Class
# It handles Single Player Game.
class SinglePlayer:

    # Constructor
    def __init__(self):
        self.board = Board()
        self.computer_mark = "X" 
        self.player_mark = "O"
        self.game_over = False
        self.turn = 0

    # Getting Player Move
    def get_player_move(self):
        try:
            # Clearing Screen
            clear_screen()
            # Printing Board
            self.board.print_board()
            # Printing Available Moves
            print()
            print(f"Available Moves are: {self.board.get_available_moves()}")
            # Getting input from the user
            row = int(input("Enter the row number > "))
            col = int(input("Enter the column number > "))

            if self.board.is_free(row, col):
                return (row, col)
            else:
                print("Invalid Move")
                raise ValueError
        except ValueError:
            # Asking if user wants to exit
            ask_exit()
            return self.get_player_move()

    # MainLoop
    def run(self):
        # Clearing Screen
        clear_screen()
        # Printing Board
        self.board.print_board()
        # Print who goes first
        print("The computer goes first.")

        while not self.game_over:
            if self.turn == 0:
                # Getting and Making Move
                move = self.get_best_move()
                self.board.make_move(*move, self.computer_mark)

                # Checking for win and tie
                # if both are false then
                # change turn
                if self.board.is_winner(self.computer_mark):
                    # Clearing Screen
                    clear_screen()
                    # Printing Board
                    self.board.print_board()
                    # Printing Who Won
                    print("X Won...")
                    self.game_over = True
                elif self.board.is_tie():
                    # Clearing Screen
                    clear_screen()
                    # Printing Board
                    self.board.print_board()
                    print("The Game is a tie...")
                    self.game_over = True
                else:
                    self.turn += 1
            else:
                # Getting and Making Move
                move = self.get_player_move()
                self.board.make_move(*move, self.player_mark)

                # Checking for win and tie
                # if both are false then
                # change turn
                if self.board.is_winner(self.player_mark):
                    # Clearing Screen
                    clear_screen()
                    # Printing Board
                    self.board.print_board()
                    # Printing Who Won
                    print("O Won...")
                    self.game_over = True
                elif self.board.is_tie():
                    # Clearing Screen
                    clear_screen()
                    # Printing Board
                    self.board.print_board()
                    print("The Game is a tie...")
                    self.game_over = True
                else:
                    self.turn -= 1


class Easy(SinglePlayer):

    # Constructor
    def __init__(self):
        super().__init__()

    # Getting the best move
    def get_best_move(self):
        return random.choice(self.board.get_available_moves())


class Medium(SinglePlayer):

    # Constructor
    def __init__(self):
        super().__init__()

    def get_corner_moves(self):
        # Getting the available moves
        available_moves = self.board.get_available_moves()
        # Corner Positions
        corner_moves = [
            (0, 0),
            (0, self.board.size - 1),
            (self.board.size - 1, 0),
            (self.board.size - 1, self.board.size - 1),
        ]

        # Checking if corners are free
        # and returning them
        for move in corner_moves:
            if move in available_moves:
                yield move

    def get_corner_move(self):
        # Checking if the board size is even
        if self.board.size % 2 == 1:
            return False
        
        # checking if the center is free then
        # return a tuple of center.
        center = (self.board.size - 1) / 2
        if self.board.is_free(center, center):
            return (center, center)

    # Getting the best move
    def get_best_move(self):
        # Checking if computer can win in one move
        for move in self.board.get_available_moves():
            # Getting the Board Copy
            board_copy = self.board.copy()
            # Making Move
            board_copy.make_move(move[0], move[1], self.computer_mark)
            # Checking if computer won
            if board_copy.is_winner(self.computer_mark):
                return move

        # Checking if player can win in one move
        for move in self.board.get_available_moves():
            # Getting board copy
            board_copy = self.board.copy()
            # Making move
            board_copy.make_move(move[0], move[1], self.player_mark)
            # Checking if player won
            if board_copy.is_winner(self.player_mark):
                return move

        # Getting corner moves
        corner_moves = self.get_corner_moves()
        # If move is not None then return move
        if corner_moves is not None:
            return random.choice(list(corner_moves))
        else:
            # Getting the board's center
            center = self.get_center_position()
            # if center is not false return center
            # else return random available move
            if center:
                return center
            else:
                return random.choice(self.board.get_available_moves())


class Impossible(SinglePlayer):

    # Constructor
    def __init__(self):
        super().__init__()

    def evaluate(self):
        pass

    def minimax(self):
        pass

    # Getting the best move
    def get_best_move(self):
        pass


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
                elif row == self.size - 1:
                    return True

        # Checking Horizontally for win
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] != mark:
                    break
                elif col == self.size - 1:
                    return True

        # Checking Diagonals for win
        for idx in range(self.size):
            if self.board[idx, idx] != mark:
                break
            elif idx == self.size - 1:
                return True

        # Checking Diagonals for win
        col = self.size
        for row in range(self.size):
            col -= 1
            if self.board[row, col] != mark:
                break
            elif row == self.size - 1:
                return True

    # Checking for Tie
    def is_tie(self):
        return len(self.get_available_moves()) == 0

    # Returns True or False
    def is_moves_left(self):
        if len(self.get_available_moves) == 0:
            return True
        else:
            return False

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
        return [value for value in zip(*np.where(self.board == self.filler))]


    # Making Board
    def make_board(self):
        board = np.zeros((self.size, self.size), dtype=int)
        return np.where(board == 0, self.filler, board)

    # Returns a copy of the board.
    def copy(self):
        board = Board()
        board.board = deepcopy(self.board)
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
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)

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
        print("Exiting Program...")
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

