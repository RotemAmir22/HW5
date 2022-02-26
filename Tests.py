import random
from unittest import TestCase

from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team


def random_hand(number, seed=12):
    """
    The function allows you to randomly allocate Hands
    :param:
        number - number of domino each hand
        seed - defined seed for random
    :return:
        list - the list contain Hand object
    """
    all_dominoes = [Domino(i, j) for i in range(7) for j in range(i, 7)]
    random.seed(seed)
    random.shuffle(all_dominoes)
    list_hands = []
    for i in range(0, len(all_dominoes), number):
        list_hands.append(Hand(all_dominoes[i:number + i]))
    return list_hands


class Tests(TestCase):
    def test_str_InvalidNumberException(self):
        try:
            raise InvalidNumberException("Invalid rang 1 - 28")
        except Exception as e:
            self.assertEqual(str(e), 'ERROR Invalid rang 1 - 28')

    def test_str_Domino(self):
        d = Domino(1, 2)
        self.assertEqual(str(d), '[1|2]')

    def test_init_board(self):
        self.assertRaises(InvalidNumberException, Board, 0)
        self.assertEqual([], Board(1).get_collection())

    def test_Board(self):
        """ Test for str, len, repr and add"""
        b = Board(4)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 3)
        d5 = Domino(1, 1)

        self.assertTrue(b.add(d1, False))
        self.assertEqual(len(b), 1)
        self.assertEqual(str(b), '[3|3]')
        self.assertEqual(repr(b), '[3|3]')

        self.assertTrue(b.add(d2, False))
        self.assertEqual(len(b), 2)
        self.assertEqual(str(b), '[4|3][3|3]')
        self.assertEqual(repr(b), '[4|3][3|3]')

        self.assertTrue(b.add(d3, False))

        self.assertEqual(len(b), 3)
        self.assertEqual(str(b), '[1|4][4|3][3|3]')
        self.assertEqual(repr(b), '[1|4][4|3][3|3]')

        self.assertTrue(b.add(d4, True))

        self.assertEqual(len(b), 4)
        self.assertEqual(str(b), '[1|4][4|3][3|3][3|1]')
        self.assertEqual(repr(b), '[1|4][4|3][3|3][3|1]')

        self.assertRaises(FullBoardException, b.add, d5, False)

    def test_str_Player(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        h = Hand([d1, d2, d3])
        p1 = NaivePlayer("shir", 26, h)
        self.assertEqual(str(p1), "Name: shir, Age: 26, Hand: [1|2][1|3][1|4], Score: 12")
        p1 = NaivePlayer("shir", 26, [])
        self.assertEqual(str(p1), 'Name: shir, Age: 26, Hand: [], Score: 0')

    def test_str_Team(self):
        list_hands = random_hand(7)
        p1 = NaivePlayer("shir", 26, list_hands[0])
        p2 = NaivePlayer("yishaia", 26, list_hands[1])
        p3 = NaivePlayer("yael", 26, list_hands[2])
        p4 = NaivePlayer("chen", 26, list_hands[3])
        t1 = Team("Blue", [p1, p2, p3, p4])
        self.assertEqual(str(t1), 'Name Blue, Score team: 168, Players: Name: shir, Age: 26, Hand: '
                                  '[2|6][4|5][3|5][0|5][0|6][0|1][1|4], Score: 42 Name: yishaia, '
                                  'Age: 26, Hand: [1|1][0|2][3|4][4|6][0|3][1|3][2|2], Score: 32 Name: yael, Age: 26, '
                                  'Hand: [3|3][2|3][5|6][6|6][4|4][0|0][1|6], Score: 49 Name: chen, Age: 26, '
                                  'Hand: [0|4][1|5][5|5][2|5][3|6][1|2][2|4], Score: 45')

    def test_play(self):
        # Game
        list_hands = random_hand(7)
        p1 = NaivePlayer("shir", 26, list_hands[0])
        p2 = NaivePlayer("yishaia", 26, list_hands[1])
        p3 = NaivePlayer("yael", 26, list_hands[2])
        p4 = NaivePlayer("chen", 26, list_hands[3])
        t1 = Team("Blue", [p1, p2, p3, p4])

        list_hands = random_hand(7, 1)
        p1 = NaivePlayer("shir", 26, list_hands[0])
        p2 = NaivePlayer("yishaia", 26, list_hands[1])
        p3 = NaivePlayer("yael", 26, list_hands[2])
        p4 = NaivePlayer("chen", 26, list_hands[3])
        t2 = Team("Red", [p1, p2, p3, p4])
        b1 = Board(28)
        g = Game(b1, t1, t2)
        self.assertEqual('Team Red wins Team Blue', g.play())
        self.assertEqual(str(b1),
         '[3|6][6|1][1|1][1|3][3|1][1|1][1|4][4|6][6|6][6|0][0|2][2|6][6|5][5|4][4|5][5|3][3|4][4|1][1|5][5|0][0|1][1|0][0|5][5|2][2|2][2|2][2|6][6|5]')
        self.assertEqual(86, t1.score_team())
        self.assertTrue(t1.has_dominoes_team())
        self.assertEqual(78, t2.score_team())
        self.assertTrue(t2.has_dominoes_team())