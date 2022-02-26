from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, age, hand):
        """
        builds a player with given input
        :param name: name of player
        :param age: age of player
        :param hand: hand player has
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        calculates the players score as the sum of the domino values.
        domino value: sum of right side and left side
        :return: score as number
        """
        score = 0
        if len(self.hand) > 0:  # no dominoes, score stays 0
            for domino in self.hand:
                if domino is None:
                    break
                score += domino.get_left()  # adds to score value of left side
                score += domino.get_right()  # adds to score value of right side
        return score

    def has_dominoes(self):
        """
        checks if the player still has dominoes in hand.
        :return: true if still hase dominoes, False if not
        """
        if len(self.hand) > 0:
            return True
        return False

    @abstractmethod
    def play(self, board):
        """
        method implemented in  classes
        :param board: board given
        """
        raise NotImplementedError("method not implemented in Player class")  # all can do it raise Exception

    def __str__(self):
        """
        returns a string representation of player with the following details:
        name, age, hand and score
        :return: string of details in format
        """
        return f"Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}"

    def __repr__(self):
        """
        returns a string representation of player using __str__ method
        :return: string of details in format
        """
        return self.__str__()
