import copy

from Player import Player


class MaxScorePlayer(Player):

    def play(self, board):
        """
        player goes over hand and sees which domino has the grates value.
        player tries to put the domino with the greatest value on the board first, right side then left side.
        if not successful tries the domino with second greatest value and so on...
        :param board: given board to try to add a domino
        :return: True if able to add, False if not
        """
        if self.has_dominoes():
            temp_hand = sorted(copy.deepcopy(self.hand.get_collection()), reverse=True)  # from maximum to minimum
            for domino in temp_hand:
                if board.add_right(domino):  # tries to add to right side
                    self.hand.remove_domino(domino)
                    return True
                elif board.add_left(domino):  # tries to add to left side
                    self.hand.remove_domino(domino)
                    return True
        return False

    def __str__(self):
        """
        returns string representation of naive player as requested in class Player: uses inherited method:
        details printed: Name, Age, Hand, Score
        also adds the sentence: I can win the game!
        :return: string of details in format
        """
        return Player.__str__(self) + ", I can win the game!"

    def __repr__(self):
        """
        uses __str__ method and prints its output.
        :return: string of details in format
        """
        return self.__str__()
