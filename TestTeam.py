from unittest import TestCase

from Board import Board
from Domino import Domino
from Exceptions import FullBoardException
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from NaivePlayer import NaivePlayer
from RandomPlayer import RandomPlayer
from Team import Team


class TestTeam(TestCase):
    def setUp(self):
        hand1 = Hand([Domino(0, 1), Domino(1, 5), Domino(4, 1), Domino(6, 3)])
        hand2 = Hand([Domino(2, 5), Domino(0, 6)])
        hand3 = Hand([Domino(0, 5), Domino(3, 2), Domino(0, 1)])
        self.naive_player1 = NaivePlayer("Rotem", 23, hand1)
        self.random_player1 = RandomPlayer("Jake", 25, hand2)
        self.max_score_player1 = MaxScorePlayer("Leo", 13, hand3)
        self.players = [self.naive_player1, self.max_score_player1, self.random_player1]
        self.players_w_out_dominoes = [NaivePlayer("Sharon", 3, Hand([])), self.random_player1, self.max_score_player1]
        self.team1 = Team("Scorpions", self.players)
        self.team2 = Team("Doors", self.players_w_out_dominoes)
        self.board1 = Board(5)
        self.board2 = Board(4)

    def test_get_team(self):
        print(" --> test: team -> method: get team ")
        self.assertEqual(str(self.players), str(self.team1.get_team()))
        self.assertEqual([], Team("empty", []).get_team())

    def test_score_team(self):
        print(" --> test: team -> method: score team ")
        self.assertEqual(45, self.team1.score_team())
        self.assertEqual(0, Team("empty", []).score_team())

    def test_has_dominoes_team(self):
        print(" --> test: team -> method: has dominoes team ")
        self.assertEqual(True, self.team1.has_dominoes_team())
        self.assertEqual(False, Team("empty", []).has_dominoes_team())
        self.assertEqual(True, self.team2.has_dominoes_team())

    def test_play(self):
        print(" --> test: team -> method: play ")
        self.assertEqual(True, self.team1.play(self.board1))
        self.assertEqual(True, self.team1.play(self.board1))
        self.assertEqual(True, self.team1.play(self.board1))
        self.assertEqual(True, self.team1.play(self.board1))
        self.assertEqual(True, self.team1.play(self.board1))
        with self.assertRaises(FullBoardException):
            self.team1.play(self.board1)
        self.assertEqual(True, self.team2.play(self.board2))
        self.assertEqual(True, self.team2.play(self.board2))
        self.assertEqual(False, self.team2.play(self.board2))

    def test_str_repr(self):
        print(" --> test: random player -> method: str/repr ")
        self.assertEqual("Name Scorpions, Score team: 45, Players: Name: Rotem, Age: 23, Hand: [0|1][1|5][4|1][6|3], "
                         "Score: 21 Name: Leo, Age: 13, Hand: [0|5][3|2][0|1], Score: 11, I can win the game! Name: "
                         "Jake, Age: 25, Hand: [2|5][0|6], Score: 13", self.team1.__str__())
        self.assertEqual("Name Doors, Score team: 24, Players: Name: Sharon, Age: 3, Hand: , Score: 0 Name: Jake, "
                         "Age: 25, Hand: [2|5][0|6], Score: 13 Name: Leo, Age: 13, Hand: [0|5][3|2][0|1], Score: 11, "
                         "I can win the game!", self.team2.__repr__())
