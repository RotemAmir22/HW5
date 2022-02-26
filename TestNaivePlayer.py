from unittest import TestCase

from Board import Board
from Domino import Domino
from Exceptions import FullBoardException
from Hand import Hand
from NaivePlayer import NaivePlayer


class TestNaivePlayer(TestCase):
    def setUp(self):
        hand1 = Hand([Domino(0, 1), Domino(2, 3), Domino(4, 1), Domino(5, 3)])
        hand2 = Hand([Domino(4, 5), Domino(2, 6)])
        self.board1 = Board(5)
        self.board1.add(Domino(3, 2))
        self.board1.add_right(Domino(2, 0))
        self.naive_player1 = NaivePlayer("Rotem", 23, hand1)
        self.naive_player2 = NaivePlayer("Keren", 12, hand2)
        self.naive_player3 = NaivePlayer("Josh", 73, Hand([]))

    def test_score(self):
        print(" --> test: naive player -> method: score ")
        self.assertEqual(19, self.naive_player1.score())
        self.assertEqual(17, self.naive_player2.score())
        self.assertEqual(0, self.naive_player3.score())

    def test_has_dominoes(self):
        print(" --> test: naive player -> method: has dominoes ")
        self.assertEqual(True, self.naive_player1.has_dominoes())
        self.assertEqual(True, self.naive_player2.has_dominoes())
        self.assertEqual(False, self.naive_player3.has_dominoes())

    def test_play(self):
        print(" --> test: naive player -> method: play ")
        self.assertEqual(True, self.naive_player1.play(self.board1))
        self.assertEqual("[2|3][4|1][5|3]", self.naive_player1.hand.__str__())
        self.assertEqual(False, self.naive_player2.play(self.board1))
        self.assertEqual(True, self.naive_player2.play(Board(12)))
        self.assertEqual(False,self.naive_player3.play(self.board1))
        self.assertEqual(True, self.naive_player1.play(self.board1))
        self.assertEqual(True, self.naive_player1.play(self.board1))
        with self.assertRaises(FullBoardException):
            self.naive_player1.play(self.board1)

    def test_str_repr(self):
        print(" --> test: naive player -> method: str/repr ")
        self.assertEqual("Name: Rotem, Age: 23, Hand: [0|1][2|3][4|1][5|3], Score: 19",self.naive_player1.__str__())
        self.assertEqual("Name: Keren, Age: 12, Hand: [4|5][2|6], Score: 17", self.naive_player2.__repr__())
        self.assertEqual("Name: Josh, Age: 73, Hand: , Score: 0", self.naive_player3.__str__())
        self.assertEqual("Name: Jason, Age: 26, Hand: [], Score: 0", (NaivePlayer("Jason", 26, []).__repr__()))

