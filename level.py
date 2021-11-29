#Miriam Wojcik
#30060965
#Quidditch game
#22.1.2019
#v 1.0
"""Current version of the Quidditch game has 5 levels
Level class keeps track of the level and check is the level the last level
It has the method to increase the level"""

class Level:
    def __init__(self):
        self._level = 1
        self._is_last = 5

    #getters and setters and attribute properties for the Level class attributes
    def get_level(self):
        return self._level

    def set_level(self, newval):
        self._level = newval

    level = property(get_level, set_level)

    def get_is_last(self):
        return self._is_last

    def set_is_last(self, newval):
        self._is_last = newval

    is_last = property(get_is_last, set_is_last)

    #increase the level method
    def increase_level(self):
        self._level += 1
