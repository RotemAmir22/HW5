from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from NaivePlayer import NaivePlayer
from RandomPlayer import RandomPlayer
from Team import Team
from Game import Game


class TestGame(TestCase):
    def setUp(self):
        hand1 = Hand([Domino(0, 2), Domino(1, 5), Domino(4, 1), Domino(6, 3)])
        hand2 = Hand([Domino(2, 5), Domino(4, 6)])
        hand3 = Hand([Domino(0, 5), Domino(2, 2), Domino(0, 1)])
        naive_player1 = NaivePlayer("Harry", 23, hand1)
        random_player1 = RandomPlayer("Rom", 25, hand2)
        max_score_player1 = MaxScorePlayer("Hermione", 13, hand3)
        players1 = [naive_player1, random_player1, max_score_player1]
        hand4 = Hand([Domino(4, 4), Domino(0, 2), Domino(0, 0)])
        hand5 = Hand([Domino(0, 5), Domino(2, 0), Domino(4, 1)])
        players2 = [NaivePlayer("Voldemort", 119, Hand([])), RandomPlayer("Bella", 46, hand4),
                    RandomPlayer("Snape", 57, hand5)]
        self.team1 = Team("Golden Trio", players1)
        self.team2 = Team("Death Eaters", players2)
        max_score_player2 = MaxScorePlayer("Susan", 32, Hand([Domino(1, 2), Domino(5, 4), Domino(0, 0)]))
        naive_player3 = MaxScorePlayer("Missing Link", 118, Hand([Domino(3, 2), Domino(1, 1), Domino(2, 0)]))
        self.team3 = Team("Monsters", [max_score_player2, naive_player3])
        self.team4 = Team("Aliens", [RandomPlayer("Gallaxhar", 6, Hand([Domino(2, 5), Domino(6, 2), Domino(6, 6)]))])
        self.team5 = Team("Only6", [RandomPlayer("Shirley", 14, Hand([Domino(6, 6), Domino(6, 6)]))])
        self.team6 = Team("One of a kind", [MaxScorePlayer("Queen B", 50, Hand([Domino(4, 5), Domino(5, 4)]))])
        self.team7 = Team("Unique", [RandomPlayer("Lady G", 36, Hand([Domino(2, 1)]))])
        self.team8 = Team("Lions", [NaivePlayer("Simba", 12, Hand([Domino(1, 0), Domino(2, 3)]))])
        self.team9 = Team("Hyenas", [MaxScorePlayer("Scar", 53, Hand([Domino(4, 1), Domino(1, 4)]))])
        self.team10 = Team("Crips", [NaivePlayer("Snoop Dogg", 50, Hand([Domino(1, 0), Domino(4, 3)]))])
        self.team11 = Team("Bloods", [NaivePlayer("Cardi B", 29, Hand([Domino(1, 4), Domino(3, 5), Domino(6, 1)]))])

    def test_play(self):
        print(" --> test: game -> method: play ")
        self.assertEqual("Team Death Eaters wins Team Golden Trio", Game(Board(7), self.team1, self.team2).play())
        self.assertEqual("Draw!", Game(Board(4), self.team2, self.team2).play())
        self.assertEqual("Team Death Eaters wins Team Golden Trio", Game(Board(8), self.team2, self.team1).play())
        self.assertEqual("Draw!", Game(Board(26), self.team4, self.team3).play())
        self.assertEqual("Team Monsters wins Team Aliens", Game(Board(20), self.team3, self.team4).play())
        self.assertEqual("Team Monsters wins Team Only6", Game(Board(22), self.team3, self.team5).play())
        self.assertEqual("Team One of a kind wins Team Unique", Game(Board(2), self.team6, self.team7).play())
        self.assertEqual("Draw!", Game(Board(2), self.team8, self.team9).play())
        self.assertEqual("Team Crips wins Team Bloods", Game(Board(6), self.team11, self.team10).play())
