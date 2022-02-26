from unittest import TestCase
from Board import Board
from Domino import Domino
from Exceptions import FullBoardException
from Hand import Hand
from RandomPlayer import RandomPlayer


class TestRandomPlayer(TestCase):
    def setUp(self):
        hand1 = Hand([Domino(5, 6), Domino(1, 1), Domino(2, 2), Domino(0, 3)])
        hand2 = Hand([Domino(0, 6), Domino(4, 4), Domino(0, 4), Domino(5, 6)])
        self.board1 = Board(3)
        self.board1.add(Domino(3, 2))
        self.random_player1 = RandomPlayer("Rotem", 23, hand1)
        self.random_player2 = RandomPlayer("Keren", 12, hand2)
        self.random_player3 = RandomPlayer("Josh", 73, Hand([]))

    def test_score(self):
        print(" --> test: random player -> method: score ")
        self.assertEqual(20, self.random_player1.score())
        self.assertEqual(29, self.random_player2.score())
        self.assertEqual(0, self.random_player3.score())

    def test_has_dominoes(self):
        print(" --> test: random player -> method: has dominoes ")
        self.assertEqual(True, self.random_player1.has_dominoes())
        self.assertEqual(True, self.random_player2.has_dominoes())
        self.assertEqual(False, self.random_player3.has_dominoes())

    def test_play(self):
        print(" --> test: random player -> method: play ")
        self.assertEqual(True, self.random_player1.play(self.board1))
        self.assertEqual("[5|6][1|1][0|3]", self.random_player1.hand.__str__())
        self.assertEqual("[0|6][4|4][0|4][5|6]", self.random_player2.hand.__str__())
        self.assertEqual(False, self.random_player2.play(self.board1))
        self.assertEqual("[0|6][4|4][0|4][5|6]", self.random_player2.hand.__repr__())
        self.assertEqual(True, self.random_player2.play(Board(12)))
        self.assertEqual(False, self.random_player3.play(self.board1))
        self.assertEqual(True, self.random_player1.play(self.board1))
        with self.assertRaises(FullBoardException):
            self.random_player1.play(self.board1)

    def test_str_repr(self):
        print(" --> test: random player -> method: str/repr ")
        self.assertEqual("Name: Rotem, Age: 23, Hand: [5|6][1|1][2|2][0|3], Score: 20", self.random_player1.__str__())
        self.assertEqual("Name: Keren, Age: 12, Hand: [0|6][4|4][0|4][5|6], Score: 29", self.random_player2.__repr__())
        self.assertEqual("Name: Josh, Age: 73, Hand: , Score: 0", self.random_player3.__str__())
        self.assertEqual("Name: Jason, Age: 26, Hand: [], Score: 0", (RandomPlayer("Jason", 26, []).__repr__()))
