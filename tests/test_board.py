from board import Board
from board import MoveOutOfBoundsException, PositionAlreadyFilledException
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def set_up_draw(self):
        """Set up a board with a tied position."""
        self.board.add_player_move(1, 8)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 7)
        self.board.add_player_move(2, 6)
        self.board.add_player_move(1, 2)
        self.board.add_player_move(2, 0)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 1)

    def test_default_board_has_3_rows(self):
        self.assertEqual(3, len(self.board._board))

    def test_default_board_has_3_columns(self):
        self.assertEqual(3, len(self.board._board[2]))

    def test_new_board_has_given_number_of_rows(self):
        size = 4
        board = Board(size)
        self.assertEqual(size, len(board._board))

    def test_new_board_given_given_number_of_columns(self):
        size = 4
        board = Board(size)
        self.assertEqual(size, len(board._board[3]))

    def test_move_added_to_correct_cell(self):
        self.board.add_player_move(1, 7)
        self.assertEqual(1, self.board._board[2][1])

    def test_move_not_added_to_incorrect_row(self):
        self.board.add_player_move(1, 0)
        self.assertEqual(0, self.board._board[1][0])

    def test_move_below_zero_fails(self):
        self.assertRaises(MoveOutOfBoundsException,
                          self.board.add_player_move, 1, -1)

    def test_move_higher_than_last_cell_number_fails(self):
        self.assertRaises(MoveOutOfBoundsException,
                          self.board.add_player_move, 1, 9)

    def test_move_fails_if_cell_already_filled(self):
        self.board.add_player_move(1, 0)
        self.assertRaises(PositionAlreadyFilledException,
                          self.board.add_player_move, 2, 0)

    def test_move_with_coordinates_added_to_correct_cell(self):
        self.board.add_move_by_coordinates(1, 2, 2)
        self.assertEqual(1, self.board._board[2][2])

    def test_move_with_coordinates_not_added_to_incorrect_row(self):
        self.board.add_move_by_coordinates(1, 2, 2)
        self.assertEqual(0, self.board._board[1][2])

    def test_move_with_row_below_zero_fails(self):
        self.assertRaises(MoveOutOfBoundsException,
                          self.board.add_move_by_coordinates, 1, -1, 1)

    def test_move_with_column_below_zero_fails(self):
        self.assertRaises(MoveOutOfBoundsException,
                          self.board.add_move_by_coordinates, 1, 1, -1)

    def test_move_with_row_higher_than_board_size_fails(self):
        self.assertRaises(MoveOutOfBoundsException,
                          self.board.add_move_by_coordinates, 1, 3, 0)

    def test_move_with_column_higher_than_board_size_fails(self):
        self.assertRaises(MoveOutOfBoundsException,
                          self.board.add_move_by_coordinates, 1, 0, 3)

    def test_move_with_coordinates_fails_if_cell_already_filled(self):
        self.board.add_move_by_coordinates(1, 0, 0)
        self.assertRaises(PositionAlreadyFilledException,
                          self.board.add_move_by_coordinates, 2, 0, 0)

    def test_horizontal_winner_found_in_first_row(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 3)
        self.board.add_player_move(1, 1)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 2)
        self.assertEqual(1, self.board.find_horizontal_winner())

    def test_horizontal_winner_found_in_last_row(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 6)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 7)
        self.board.add_player_move(1, 4)
        self.board.add_player_move(2, 8)
        self.assertEqual(2, self.board.find_horizontal_winner())

    def test_horizontal_winner_not_found_in_empty_row(self):
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 6)
        self.board.add_player_move(1, 4)
        self.board.add_player_move(2, 7)
        self.board.add_player_move(1, 5)
        self.assertEqual(1, self.board.find_horizontal_winner())

    def test_no_horizontal_winner_found_in_empty_board(self):
        self.assertEqual(0, self.board.find_horizontal_winner())

    def test_no_horizontal_winner_found_in_draw(self):
        self.set_up_draw()
        self.assertEqual(0, self.board.find_horizontal_winner())

    def test_vertical_winner_found_in_first_column(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 1)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 6)
        self.assertEqual(1, self.board.find_vertical_winner())

    def test_vertical_winner_found_in_last_column(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 2)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 7)
        self.board.add_player_move(2, 8)
        self.assertEqual(2, self.board.find_vertical_winner())

    def test_no_vertical_winner_found_in_empty_board(self):
        self.assertEqual(0, self.board.find_vertical_winner())

    def test_no_vertical_winner_found_in_draw(self):
        self.set_up_draw()
        self.assertEqual(0, self.board.find_vertical_winner())

    def test_vertical_winner_not_found_in_empty_column(self):
        self.board.add_player_move(1, 1)
        self.board.add_player_move(2, 2)
        self.board.add_player_move(1, 4)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 7)
        self.assertEqual(1, self.board.find_vertical_winner())

    def test_rightward_diagonal_winner_found(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 1)
        self.board.add_player_move(1, 4)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 8)
        self.assertEqual(1, self.board.find_diagonal_winner())

    def test_leftward_diagonal_winner_found(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 2)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 6)
        self.board.add_player_move(1, 8)
        self.board.add_player_move(2, 4)
        self.assertEqual(2, self.board.find_diagonal_winner())

    def test_no_diagonal_winner_found_in_empty_board(self):
        self.assertEqual(0, self.board.find_diagonal_winner())

    def test_no_diagonal_winner_found_in_draw(self):
        self.set_up_draw()
        self.assertEqual(0, self.board.find_diagonal_winner())

    def test_find_winner_finds_horizontal_winner(self):
        self.board.add_player_move(1, 6)
        self.board.add_player_move(2, 3)
        self.board.add_player_move(1, 7)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 8)
        self.assertEqual(1, self.board.find_winner())

    def test_find_winner_finds_vertical_winner(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 2)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 7)
        self.board.add_player_move(2, 8)
        self.assertEqual(2, self.board.find_winner())

    def test_find_winner_finds_diagonal_winner(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 1)
        self.board.add_player_move(1, 4)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 8)
        self.assertEqual(1, self.board.find_winner())

    def test_find_winner_finds_no_winner(self):
        self.assertEqual(0, self.board.find_winner())

    def test_empty_board_is_not_full(self):
        self.assertFalse(self.board.is_board_full())

    def test_drawn_board_is_full(self):
        self.set_up_draw()
        self.assertTrue(self.board.is_board_full())

    def test_partially_filled_board_is_not_full(self):
        self.board.add_player_move(1, 2)
        self.board.add_player_move(2, 3)
        self.board.add_player_move(1, 7)
        self.assertFalse(self.board.is_board_full())

    def test_max_move_calculated_correctly(self):
        self.assertEqual(8, self.board.get_maximum_move())
