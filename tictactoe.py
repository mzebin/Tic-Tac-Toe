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
                print(move)
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
                move = self.board.get_player_move(self.player_mark)
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
            board_copy.make_move(*move, self.computer_mark)
            # Checking if computer won
            if board_copy.is_winner(self.computer_mark):
                return move

        # Checking if player can win in one move
        for move in self.board.get_available_moves():
            # Getting board copy
            board_copy = self.board.copy()
            # Making move
            board_copy.make_move(*move, self.player_mark)
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

    # Returns the score based the winner.
    def evaluate(self):
        # Returning 10 if computer wins
        # Returning -10 if player wins
        # Returning 0 if it is a tie.
        if self.board.is_winner(self.computer_mark):
            return 10
        elif self.board.is_winner(self.player_mark):
            return -10
        elif self.board.is_tie():
            return 0

    def minimax(self, depth, is_max):
        # Evaluating the Score
        score = self.evaluate()

        # Returning the score when the game is over.
        if score == 10 or score == -10 or score == 0:
            return score

        if is_max:
            best = float("-inf")

            # Looping through all the available moves
            for move in self.board.get_available_moves():
                self.board.make_move(*move, self.computer_mark)
                best = max(best, self.minimax(depth + 1, not is_max))
                self.board.undo_move(*move)
        else:
            best = float("inf")

            # Looping through all the available moves.
            for move in self.board.get_available_moves():
                self.board.make_move(*move, self.player_mark)
                best = min(best, self.minimax(depth + 1, not is_max))
                self.board.undo_move(*move)

        return best

    # Getting the best move
    def get_best_move(self):
        best_val = float("-inf")
        best_move = ()

        # Finding the best move.
        # Looping through all the available moves.
        for move in self.board.get_available_moves():
            # Checking if cell is free.
            if self.board.is_free(*move):
                # Making a move, calculating its value
                # and Undoing the move.
                self.board.make_move(*move, self.computer_mark)
                value = self.minimax(0, False)
                self.board.undo_move(*move)

                # Changing the best value and best move
                # if value is better than best_val.
                if value > best_val:
                    best_val = value
                    best_move = move

        return best_move

# The Multiplayer Class
# It handles multiplayer game.
class MultiPlayer:

    # Constructor
    def __init__(self):
        self.board = Board()
        self.marks = ["X", "O"]
        self.game_over = False
        self.turn = 0

    def run(self):
        while not self.game_over:
            move = self.board.get_player_move(self.marks[self.turn])
            self.board.make_move(*move, self.marks[self.turn])

            # Checking for winner
            if self.board.is_winner(self.marks[self.turn]):
                clear_screen()
                self.board.print_board()
                print(self.marks[self.turn], "Won...")
                self.game_over = True
            # Checking for tie
            if self.board.is_tie():
                clear_screen()
                self.board.print_board()
                print("The Game is a tie...")
                self.game_over = True
            # Swaping turn
            self.turn = 0 if self.turn == 1 else 1


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
            else:
                return True

        # Checking Horizontally for win
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row, col] != mark:
                    break
            else:
                return True

        # Checking Diagonals for win
        for idx in range(self.size):
            if self.board[idx, idx] != mark:
                break
        else:
            return True

        # Checking Diagonals for win
        col = self.size
        for row in range(self.size):
            col -= 1
            if self.board[row, col] != mark:
                break
        else:
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
    def undo_move(self, row, col):
        self.board[row, col] = self.filler

    # Getting Player Move
    def get_player_move(self, mark):
        try:
            # Clearing Screen
            clear_screen()
            # Printing Board
            self.print_board()
            # Printing Available Moves
            print()
            print(f"Available Moves are: {self.get_available_moves()}")
            print(f"{mark}'s turn")
            # Getting input from the user
            row = int(input("Enter the row number > "))
            col = int(input("Enter the column number > "))

            if self.is_free(row, col):
                return (row, col)
            else:
                print("Invalid Move")
                raise ValueError
        except ValueError:
            # Asking if user wants to exit
            ask_exit()
            return self.get_player_move(mark)

    # Returns the available moves
    def get_available_moves(self):
        return np.argwhere(self.board == self.filler).tolist()


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

