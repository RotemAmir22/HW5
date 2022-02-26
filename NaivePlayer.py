from Player import Player


class NaivePlayer(Player):

    def play(self, board):
        """
        goes over its hand from index 0 till the end.
        for every domino naive player tries to place it on the right side, then the left side.
        if player is able to add domino, method removes the domino from the hand and return True, else returns False.
        :param board: given board to try to add a domino
        :return: True if able to add, False if not
        """
        if self.has_dominoes():
            for domino in self.hand.get_collection():
                if board.add_right(domino):  # tries to add to right side
                    self.hand.remove_domino(domino)
                    return True
                elif board.add_left(domino):  # tries to add to left side
                    self.hand.remove_domino(domino)
                    return True
        return False
