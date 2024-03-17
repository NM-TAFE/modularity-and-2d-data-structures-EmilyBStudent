"""Provides a class representing a Tic-Tac-Toe game board and its state"""

from utilities import all_items_in_collection_equal
import math


class Board:
    """A Tic-Tac-Toe game board and its current state"""

    def __init__(self, size: int = 3) -> None:
        """
        Initialise the Tic-Tac-Toe game board with the given size (defaults to
        3).
        :param size: The size of the game board on each side (the board is
            always square)
        """
        self.size = size
        self.empty = 0
        self._minimum_move = 0
        self._maximum_move = self.size*self.size - 1
        self.construct_board(size)

    def construct_board(self, size: int) -> None:
        """
        Construct a 2D data structure of the given size, to maintain the state
        of the game board
        :param size: The size of the game board on each side (the board is
            always square)
        """
        self._board = []
        for row_number in range(0, size):
            row = [self.empty] * size
            self._board.append(row)

    def get_board_data(self) -> list[list]:
        """
        Return the 2D data structure representing the board state.
        :returns: the data in self._board
        """
        return self._board

    def add_player_move(self, player: int, move: int) -> bool:
        """
        Add the given player's chosen move to the board.
        :param player: the player making their move, represented as an integer.
        :param move: the player's chosen move, represented as an integer
            between 0 and the number of cells on the board minus 1.
        :returns: True if the move was successful, False if the move is invalid
            based on the board state.
        """
        # The move is provided as an integer from 0 to the total number of
        # cells on the board, so we need to convert it into indices for a
        # 2-dimensional data structure.
        row = math.floor(move / self.size)
        column = move % self.size
        return self.add_move_by_coordinates(player, row, column)

    def add_move_by_coordinates(self, player: int, row: int,
                                column: int) -> bool:
        """
        Add the given player's chosen move to the board, using coordinates
        to identify the move on the board.
        :param player: the player making their move, represented as an integer.
        :param row: the row number of the player's chosen move.
        :param column: the column number of the player's chosen move.
        :returns: True if the move was successful, False if the move is invalid
            based on the board state.
        """
        if row < 0 or column < 0:
            return False
        if row >= self.size or column >= self.size:
            return False
        if self._board[row][column] != self.empty:
            return False
        
        self._board[row][column] = player
        return True

    def find_winner(self) -> int:
        """
        Check for all possible win conditions.
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        winner = self.find_horizontal_winner()
        if winner != 0:
            return winner
        winner = self.find_vertical_winner()
        if winner != 0:
            return winner
        winner = self.find_diagonal_winner()
        return winner

    def find_horizontal_winner(self) -> int:
        """
        Check for win conditions on the horizontal/in the rows.
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        for row in self._board:
            if row[0] != 0 and all_items_in_collection_equal(row):
                return row[0]
        return 0

    def find_vertical_winner(self) -> int:
        """
        Check for win conditions on the vertical/in the columns.
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        for column in range(0, self.size):
            column_data = []
            for row in range(0, self.size):
                column_data.append(self._board[row][column])
            if column_data[0] != 0 and all_items_in_collection_equal(column_data):
                return column_data[0]
        return 0

    def find_diagonal_winner(self) -> int:
        """
        Check for win conditions on the two longest diagonals (passing through
        the centre of the board).
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        diagonal_data = []
        for row_and_column in range(0, self.size):
            diagonal_data.append(self._board[row_and_column][row_and_column])
        if (diagonal_data[0] != 0 and
                all_items_in_collection_equal(diagonal_data)):
            return diagonal_data[0]

        diagonal_data = []
        column = self.size - 1
        for row in range(0, self.size):
            diagonal_data.append(self._board[row][column])
            column -= 1
        if (diagonal_data[0] != 0 and
                all_items_in_collection_equal(diagonal_data)):
            return diagonal_data[0]
        return 0

    def is_board_full(self) -> bool:
        """
        Check whether the board is full (so that no more moves can be made).
        :returns: True if the board is full, False if not.
        """
        for row in self._board:
            if self.empty in row:
                return False
        return True

    def get_maximum_move(self) -> int:
        """
        Returns the highest move allowable on this board.
        :returns: The maximum move allowable on the board.
        """
        return self._maximum_move

    def get_minimum_move(self) -> int:
        """
        Return the lowest-numbered move allowable on this board.
        :returns: the minimum move allowable on this board.
        """
        return self._minimum_move
