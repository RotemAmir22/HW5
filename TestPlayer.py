from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = NaivePlayer("Rotem", 23, Hand([Domino(1, 2), Domino(3, 4), Domino(5, 5)]))
        self.player2 = NaivePlayer("Ido", 19, Hand([Domino(6, 4), Domino(3, 2), Domino(1, 0)]))
        self.player3 = NaivePlayer("Danny", 53, Hand([]))

        self.board1 = Board(4)
        self.board1.add(Domino(1, 2))
        self.board1.add(Domino(2, 5))
        self.board1.add(Domino(3, 1), False)

    def test_score(self):
        print(" --> test: player -> method: score ")
        self.assertEqual(20, self.player1.score())
        self.assertEqual(16, self.player2.score())
        self.assertEqual(0, self.player3.score())

    def test_has_dominoes(self):
        print(" --> test: player -> method: has dominoes ")
        self.assertEqual(True, self.player1.has_dominoes())
        self.assertEqual(True, self.player2.has_dominoes())
        self.assertEqual(False, self.player3.has_dominoes())

    def test_str_repr(self):
        print(" --> test: player -> method: str/repr ")
        self.assertEqual("Name: Rotem, Age: 23, Hand: [1|2][3|4][5|5], Score: 20", self.player1.__str__())
        self.assertEqual("Name: Ido, Age: 19, Hand: [6|4][3|2][1|0], Score: 16", self.player2.__repr__())
        self.assertEqual("Name: Danny, Age: 53, Hand: , Score: 0", self.player3.__str__())
