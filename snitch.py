#Miriam Wojcik
#30060965
#Quidditch game
#22.1.2019
#v 1.0
"""The objective of the Quidditch game is for the Seekers to catch the Snitch ball, which is a golden, flying ball
The Snitch class represents the Golden Snitch ball and has such attributes as row and column (coordinates on the map)
as well as the char attribute (used to represent the Golden Snitch on the map)"""

#import random module
import random

#define the Snitch class. Snitch class attributes: row, col, char
class Snitch:
    def __init__(self):
        #self._row = 5
        self._row = 10
        #self._col = 7
        self._col = 7
        self._char = '*'


    #getters, setters and attributes properties for accessing the attributes
    def get_row(self):
        return self._row

    def set_row(self, newval):
        self._row = newval

    row = property(get_row, set_row)

    def get_col(self):
        return self._col

    def set_col(self, newval):
        self._col = newval

    col = property(get_col, set_col)

    def get_char(self):
        return self._char

    def set_char(self, newval):
        self._char = newval

    snitch_char = property(get_char, set_char)


    #fly function, which uses the random module to allow the Golden Snitch to move on the map in the random direction
    def fly(self):
        direction = random.choice([(+1), (-1)])
        choice = random.choice([self._row, self._col])
        if choice == self._row:
            self._row += direction
        elif choice == self._col:
            self._col += direction





