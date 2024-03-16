"""
Tic-Tac-Toe game manager. This provides a GameManager class which contains the
basic program flow and gameplay loop for a game of Tic-Tac-Toe.
"""

from board import Board
from console_ui import ConsoleUI


class GameManager:
    """
    Tic-Tac-Toe game manager class. This provides the basic program flow and
    gameplay loop for a game of Tic-Tac-Toe.
    """

    def __init__(self):
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
        self.MAX_MOVE = self.board.get_max_move()
        self.ui = ConsoleUI(self.player_map)

    def main(self):
        """The main gameplay loop for the Tic-Tac-Toe game"""
        # Game loop
        while True:
            self.display_board()

            if self.check_for_winner():
                return
            if self.check_for_tie():
                return

            # Get next move
            while True:
                move = self.ui.get_current_player_move(self.current_player,
                                                       self.MAX_MOVE)
                if 0 <= int(move) and self.board.add_player_move(self.current_player, move):
                    break
                else:
                    self.ui.show_invalid_move_error()

            self.switch_players()

    def display_board(self):
        """Display the current state of the game board."""
        self.ui.display_2d_board(self.board.get_board_data())

    def check_for_winner(self):
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

    def check_for_tie(self):
        """
        Check if the game has ended in a tie. If so, announce the fact to the
        players
        :returns: True if the game has ended in a tie, False if not
        """
        if self.board.is_board_full():
            self.ui.announce_tie()
            return True
        return False

    def switch_players(self):
        """Switch to the next player's turn."""
        if self.current_player == self.number_of_players:
            self.current_player = 1
        else:
            self.current_player += 1


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.main()