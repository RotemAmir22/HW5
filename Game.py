from Exceptions import FullBoardException


class Game:
    def __init__(self, board, team1, team2):
        """
        build the game based on the inputs:
        :param board: given board to play on
        :param team1: given team one
        :param team2: given team two
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
        how the games goes (steps):
        1. each team tries to lay a domino on the board, starting from team 1.
        2. game ends if one of the teams cant play of one team doesnt have any dominoes.
        3. the winner is the team with the lowest score
        :return: which team won vs losing team, or if there is a draw
        """
        while self.team1.has_dominoes_team() and self.team2.has_dominoes_team():  # both team have dominoes
            try:
                self.team1.play(self.board)  # team 1 plays
                self.team2.play(self.board)  # team 2 plays
                if not self.team1.play(self.board) or not self.team2.play(self.board):
                    break
            except FullBoardException:  # if the board is full, needs to catch the error
                if self.team1.score_team() < self.team2.score_team():
                    return f"Team {self.team1.name} wins Team {self.team2.name}"
                elif self.team1.score_team() > self.team2.score_team():
                    return f"Team {self.team2.name} wins Team {self.team1.name}"
                else:
                    return "Draw!"

        """when entering except, code after cant be executed"""
        if self.team1.score_team() < self.team2.score_team():
            return f"Team {self.team1.name} wins Team {self.team2.name}"
        elif self.team1.score_team() > self.team2.score_team():
            return f"Team {self.team2.name} wins Team {self.team1.name}"
        else:
            return "Draw!"
