"""
Tic-Tac-Toe game manager. This provides a GameManager class which contains the
basic program flow and gameplay loop for a game of Tic-Tac-Toe.
"""

from board import Board
from board import MoveOutOfBoundsException, PositionAlreadyFilledException
from console_ui import ConsoleUI


class GameManager:
    """
    Tic-Tac-Toe game manager class. This provides the basic program flow and
    gameplay loop for a game of Tic-Tac-Toe.
    """

    def __init__(self) -> None:
        """Initialise the Tic-Tac-Toe game"""
        # Map player numbers to visual representation as single characters of
        # text. 0 represents an empty space.
        self.player_map = {
            0: ' ',
            1: 'X',
            2: 'O',
        }
        self.number_of_players = len(self.player_map) - 1
        self.current_player = 1

        self.board = Board()
        self._minimum_move = self.board.get_minimum_move()
        self._maximum_move = self.board.get_maximum_move()
        self.ui = ConsoleUI(self.player_map)

    def main(self) -> None:
        """The main gameplay loop for the Tic-Tac-Toe game"""
        while True:
            self.display_board()
            if self.check_for_winner():
                return
            if self.check_for_tie():
                return
            self.take_current_player_turn()
            self.switch_players()

    def display_board(self) -> None:
        """Display the current state of the game board."""
        self.ui.display_2d_board(self.board.get_board_data())

    def check_for_winner(self) -> bool:
        """
        Check if one of the players has won the game. If so, announce the
        winner.
        :returns: True if a winner is found, False if not
        """
        winner = self.board.find_winner()
        if winner:
            self.ui.announce_winner(winner)
            return True
        return False

    def check_for_tie(self) -> bool:
        """
        Check if the game has ended in a tie. If so, announce the fact to the
        players
        :returns: True if the game has ended in a tie, False if not
        """
        if self.board.is_board_full():
            self.ui.announce_tie()
            return True
        return False

    def take_current_player_turn(self) -> None:
        """Get the current player's chosen move and action it."""
        while True:
            move = self.ui.get_current_player_move(self.current_player,
                                                   self._minimum_move,
                                                   self._maximum_move)
            try:
                if self.board.add_player_move(self.current_player, move):
                    return
            except MoveOutOfBoundsException:
                self.ui.show_invalid_move_error()
            except PositionAlreadyFilledException:
                self.ui.show_invalid_move_error()

    def switch_players(self) -> None:
        """Switch to the next player's turn."""
        if self.current_player == self.number_of_players:
            self.current_player = 1
        else:
            self.current_player += 1


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.main()
