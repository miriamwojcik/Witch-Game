#Miriam Wojcik
#30060965
#Quidditch game
#22.1.2019
#v 1.0
"""Game class stores teams final scores as integers and the final winner as a String"""

class Game:
    def __init__(self):
        self._team1_score = 0
        self._team2_score = 0
        self._winner = ""

#getters and setters and attributes properies for all Game class attributes
    def get_team1_score(self):
        return self._team1_score

    def set_team1_score(self, newval):
        self._team1_score = newval

    team1_score = property(get_team1_score, set_team1_score)

    def get_team2_score(self):
        return self._team2_score

    def set_team2_score(self, newval):
        self._team2_score = newval

    team2_score = property(get_team2_score, set_team2_score)

    def get_winner(self):
        return self._winner

    def set_winner(self, newval):
        self._winner = newval

    winner = property(get_winner, set_winner)

    #method returns the string with the name of the winning team and the word WINS! / used to display the winner of the game on the screen
    def winner_string(self):
        winner_string = self._winner + " WINS!"
        return winner_string