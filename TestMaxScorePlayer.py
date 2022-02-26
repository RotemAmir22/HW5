from unittest import TestCase

from Board import Board
from Domino import Domino
from Exceptions import FullBoardException
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer


class TestMaxScorePlayer(TestCase):
    def setUp(self):
        hand1 = Hand([Domino(5, 3), Domino(2, 6), Domino(4, 3), Domino(1, 6)])
        hand2 = Hand([Domino(4, 4), Domino(2, 6),Domino(0,4)])
        self.board1 = Board(3)
        self.board1.add(Domino(1, 3))
        self.max_score_player1 = MaxScorePlayer("Rotem", 23, hand1)
        self.max_score_player2 = MaxScorePlayer("Keren", 12, hand2)
        self.max_score_player3 = MaxScorePlayer("David", 73, Hand([]))

    def test_score(self):
        print(" --> test: max score player -> method: score ")
        self.assertEqual(30, self.max_score_player1.score())
        self.assertEqual(20, self.max_score_player2.score())
        self.assertEqual(0, self.max_score_player3.score())

    def test_has_dominoes(self):
        print(" --> test: max score player -> method: has dominoes ")
        self.assertEqual(True, self.max_score_player1.has_dominoes())
        self.assertEqual(True, self.max_score_player2.has_dominoes())
        self.assertEqual(False, self.max_score_player3.has_dominoes())

    def test_play(self):
        print(" --> test: max score player -> method: play ")
        self.assertEqual(True, self.max_score_player1.play(self.board1))
        self.assertEqual("[2|6][4|3][1|6]", self.max_score_player1.hand.__str__())
        self.assertEqual(False, self.max_score_player2.play(self.board1))
        self.assertEqual(True, self.max_score_player2.play(Board(2)))
        self.assertEqual(False, self.max_score_player3.play(self.board1))
        self.assertEqual(True, self.max_score_player1.play(self.board1))
        with self.assertRaises(FullBoardException):
            self.max_score_player1.play(self.board1)

    def test_str_repr(self):
        print(" --> test: max score player -> method: str/repr ")
        self.assertEqual("Name: Rotem, Age: 23, Hand: [5|3][2|6][4|3][1|6], Score: 30, I can win the game!",
                         self.max_score_player1.__str__())
        self.assertEqual("Name: Keren, Age: 12, Hand: [4|4][2|6][0|4], Score: 20, I can win the game!",
                         self.max_score_player2.__repr__())
        self.assertEqual("Name: David, Age: 73, Hand: , Score: 0, I can win the game!",
                         self.max_score_player3.__str__())
        self.assertEqual("Name: Jason, Age: 26, Hand: [], Score: 0, I can win the game!",
                         (MaxScorePlayer("Jason", 26, []).__repr__()))
