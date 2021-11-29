#Miriam Wojcik
#30060965
#Quidditch game
#22.1.2019
#v 1.0
"""Each team in the Quidditch is made of 7 players:
1 Seeker
1 Keeper
2 Beaters
3 Chasers
Team class represents the quidditch team
Aggregation of the Keeper, Seeker, Beater and Chaser class objects
Classes own attributes: team_name(string), team_score(integer)"""

#import classes Keeper, Seeker, Beater, Chaser
from player import Keeper, Seeker, Beater, Chaser

class Team(object):
    def __init__(self, team_name):
        self._team_name = team_name
        self._team_score = 0
        self.keeper = Keeper('char')
        self.seeker = Seeker('char')
        self.chaser1 = Chaser('char')
        self.chaser2 = Chaser('char')
        self.chaser3 = Chaser('char')
        self.beater1 = Beater('char')
        self.beater2 = Beater('char')

    #getters and setters and attribute properties for the Team class attributes
    def get_team_name(self):
        return self._team_name

    def set_team_name(self, newval):
        self._team_name = newval

    team_name = property(get_team_name, set_team_name)

    def get_team_score(self):
        return self._team_score

    def set_team_score(self, newval):
        self._team_score = newval

    team_score = property(get_team_score, set_team_score)

    #function to update the score, used to add 150 points to the team that wins the level
    def update_score(self):
        self.team_score += 150
