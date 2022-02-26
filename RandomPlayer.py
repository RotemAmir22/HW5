import copy
import random
from Player import Player


class RandomPlayer(Player):
    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        """
        random player shuffles its hand and then goes over it:
        goes over hand from index 0 till the end.
        for every domino naive player tries to place it on the right side, then the left side.
        if player is able to add domino, method removes the domino from the hand and return True, else returns False.
        :param board: given board to try to add a domino
        :return: True if able to add, False if not
        """
        if self.has_dominoes():
            temp_hand = copy.deepcopy(self.hand.get_collection())
            random.shuffle(temp_hand)
            for domino in temp_hand:
                if board.add_right(domino):  # tries to add to right side
                    self.hand.remove_domino(domino)
                    return True
                elif board.add_left(domino):  # tries to add to left side
                    self.hand.remove_domino(domino)
                    return True
        return False


