import copy


class Team:
    def __init__(self, name, players):
        """
        creates team with the following details inputted:
        team name and players
        :param name: team name
        :param players: players in team
        """
        self.name = name
        self.__players = players  # private attribute

    def get_team(self):
        """
        returns a deep copy of team so no user can change team or team players.
        :return: deep copy of players
        """
        return copy.deepcopy(self.__players)

    def score_team(self):
        """
        calculates the team score: sums the players scores
        :return: team score
        """
        score = 0
        for player in self.get_team():
            score += player.score()
        return score

    def has_dominoes_team(self):
        """
        checks if there is at least on player with dominoes.
        :return: True if at least on has dominoes, False if none have
        """
        for player in self.get_team():
            if player.has_dominoes():
                return True
        return False

    def play(self, board):
        """
        team plays in this order: the first player in team (index 0 in array) plays, if not able to play the turn
        goes to next in array (index + 1) and so on until someone is successful.
        if no one is able to play, method returns False
        :param board:given board to try to add a domino to
        :return: True if domino added and False if not
        """
        for player in self.__players:
            if player.play(board):
                return True
        return False

    def __str__(self):
        """
        returns a string representation of team with the following details:
        team name, team score and players with the players details.
        :return: string representation of team
        """
        temp_team = ""  # temp string
        count = 0  # before the first object, no need to add a space so count when passed first object
        for player in self.get_team():
            if count == 0:
                temp_team += player.__str__()
                count += 1  # passed first object
            else:
                temp_team += ' '
                temp_team += player.__str__()

        return f"Name {self.name}, Score team: {self.score_team()}, Players: {temp_team}"

    def __repr__(self):
        """
        returns a string version of team using __str__ method
        :return: string representation of team
        """
        return self.__str__()
