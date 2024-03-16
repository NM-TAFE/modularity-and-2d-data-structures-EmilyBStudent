from game_manager import GameManager
import unittest


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.game_manager = GameManager()

    def test_current_player_incremented_by_1(self):
        self.game_manager.switch_players()
        self.assertEqual(2, self.game_manager.current_player)

    def test_current_player_loops_back_to_1(self):
        self.game_manager.switch_players()
        self.game_manager.switch_players()
        self.assertEqual(1, self.game_manager.current_player)
