#Miriam Wojcik
#30060965
#Quidditch game
#22.1.2019
#v 1.0
"""Each team in Quidditch has 7 players. The Player class has following attributes: player_name(string),
player_char (which needs to be defined when creating an object from Player class, position(string),
row and col (integers for coordinates on the map)
Parent class for each position subclasses"""

#import random module
import random

class Player:
    def __init__(self, player_char):
        self._player_name = ''
        self._player_char = player_char
        self._position = ""
        self._row = 2
        self._col = 2

    #getters and setters and attribute properties for all attributes of the Player class
    def get_player_name(self):
        return self._player_name

    def set_player_name(self, newval):
        self._player_name = newval

    player_name = property(get_player_name, set_player_name)

    def get_plyer_char(self):
        return self._player_char

    def set_player_char(self, newval):
        self._player_char = newval

    player_char = property(get_plyer_char, set_player_char)

    def get_player_position(self):
        return self._position

    def set_player_position(self, newval):
        self._position = newval

    player_position = property(get_player_position, set_player_position)

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

    #fly function, which uses the random module to allow players to move in the random direction on the map
    def fly(self):
        direction = random.choice([(+1), (-1)])
        choice = random.choice([self._row, self._col])
        if choice == self._row:
            self._row += direction
        elif choice == self._col:
            self._col += direction

"""Seeker class is a child of the player class. The goal of Seekers in the game is to catch the Golden Snitch
The class has additional attribute of the snitch_caught and sets the player position to 'Seeker'"""
class Seeker(Player):
    def __init__(self, player_char):
        super().__init__(player_char = player_char)
        self._snitch_caught = False
        self._position = 'Seeker'

    #getters and setters and attribute properties for all attributes of the Seeker class
    def get_snitch_caught(self):
        return self._snitch_caught

    def set_snitch_caught(self, newval):
        self._snitch_caught = newval

    snitch_caught = property(get_snitch_caught, set_snitch_caught)

    def catch_snitch(self, caught):
        if caught:
            self._snitch_caught = True


    #a method which allows the human player to move the Seeker in the specified direction
    #the method overrides the fly() function in the Player class
    def fly(self, direction):
        if direction == 'left':
            self.col -= 1

        elif direction == 'right':
            self.col += 1

        elif direction == 'up':
            self.row -= 1

        elif direction == 'down':
            self.row += 1

"""Chaser is a child class of the Player class. It sets the position to 'Chaser'"""
class Chaser(Player):
    def __init__(self, player_char):
        super().__init__(player_char = player_char)
        self._position = 'Chaser'

"""Keeper is a child class of the Player class. It sets the position to 'Keeper'"""
class Keeper(Player):
    def __init__(self, player_char):
        super().__init__(player_char = player_char)
        self._position = 'Keeper'

"""Beater is a child class of the Player class. It sets the position to 'Beater'"""
class Beater(Player):
    def __init__(self, player_char):
        super().__init__(player_char = player_char)
        self._position = 'Beater'

