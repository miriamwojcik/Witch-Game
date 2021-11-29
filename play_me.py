#Miriam Wojcik
#30060965
#Quidditch game
#22.1.2019
#v 1.0
"""File contains the main program for the quidditch game"""

#import relevant modules and classes
import random
import pygame
import sys
import os
import copy
from pygame.locals import *
from pitch import Pitch
from level import Level
from team import Team
from snitch import Snitch
from player import *
from game import Game

#initialize pygame and font modules
pygame.init()
pygame.font.init()

#set FPS and initialize the fps clock
FPS = 60
fps_clock = pygame.time.Clock()

#window and display height and width / tile dimensions
width =  600
height = 600
half_height = int(height / 2 + 50)
half_width = int(width / 2)
screen_dimension = (width, height)
screen = pygame.display.set_mode(screen_dimension)
tile_height = 32
tile_width = 32
tile_floor_height = 32

#program title
pygame.display.set_caption("Quidditch by M.W. v 1.0") #tytuł okna

#background and txt colors, fonts settings
mint = (229,255,205)
blue = (170, 170, 170)
red_txt = (139,0,0)
blue_txt = (12, 36, 97)
black_txt = (0, 0, 0)
white_txt = (255, 255, 255)
bg_color =  mint

bold_txt = pygame.font.SysFont("Arial",16)
bold_txt.set_bold(True)
font = pygame.font.SysFont("Arial",20)
small_font = pygame.font.SysFont("Arial",12)
#winner font
w_font = pygame.font.SysFont("Arial", 40)


#images dictionary and mapping
img_dict = {'grass': pygame.image.load("img/grass.gif"),
            'wall': pygame.image.load("img/barrier2.gif"),
            'snitch': pygame.image.load("img/snitch.gif"),
            'seeker1': pygame.image.load("img/s1.gif"),
            'seeker2': pygame.image.load("img/s2.gif"),
            't1_player': pygame.image.load("img/p1.gif"),
            't2_player': pygame.image.load("img/p2.gif")}

tile_mapping = { '#':img_dict['wall'],
                 ' ':img_dict['grass'],
                 '$':img_dict['seeker1'],
                 '9':img_dict['seeker2'],
                 '*':img_dict['snitch'],
                 '1':img_dict['t1_player'],
                 '2':img_dict['t2_player']
                 }

#function checks did the seeker moved to the field with the Snitch (caught the Snitch)
#if the snitch has been caught set seeker.snitch_caught to True and updates the team score
def snitch_caught(seeker):
    if p.is_target(seeker.row, seeker.col) is True:
        seeker.snitch_caught = True
        if seeker == s1:
            print(s1.player_name + " catches the Golden Snitch")
            print("150 points for " + t1.team_name)
            t1.update_score()
        elif seeker == s2:
            print(s2.player_name + " catches the Golden Snitch")
            print("150 points for " + t2.team_name)
            t2.update_score()

#function to load the next level
#sets coordinates for players, Snitch and obstacles according to the level
def load_level(level):
    global player1_moves
    global player2_moves
    print("Level " + str(level))
    #reset players moves
    player1_moves = 0
    player2_moves = 0
    #reset snitch_caught property to False for both Seekers
    s1.snitch_caught = False
    s2.snitch_caught = False

    #Level 2: both seekers, Golden Snitch and 1 Beater for each team as an obstacle (Beaters do not move)
    if level == 2:
        snitch.col = 11
        snitch.row = 6
        p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)
        s1.row = 1
        s1.col = 3
        s2.row = 12
        s2.col = 2
        t1.beater1.row = 11
        t1.beater1.col = 3
        t2.beater1.row = 3
        t2.beater1.col = 5
        p.place_player(s1.player_char, s1.row, s1.col)
        p.place_player(s2.player_char, s2.row, s2.col)
        p.place_player(t1.beater1.player_char, t1.beater1.row, t1.beater1.col)
        p.place_player(t2.beater1.player_char, t2.beater2.row, t2.beater2.col)

    #Level 3: both Seekers, Golden Snitch and 2 Beaters for each team as obstacles (Beaters do not move)
    elif level == 3:
        snitch.col = 9
        snitch.row = 12
        p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)
        s1.row = 2
        s1.col = 2
        s2.row = 3
        s2.col = 2
        t1.beater1.row = 9
        t1.beater1.col = 6
        t2.beater1.row = 8
        t2.beater1.col = 10
        t1.beater2.row = 7
        t1.beater2.col = 12
        t2.beater2.row = 5
        t2.beater2.col = 5
        p.place_player(s1.player_char, s1.row, s1.col)
        p.place_player(s2.player_char, s2.row, s2.col)
        p.place_player(t1.beater1.player_char, t1.beater1.row, t1.beater1.col)
        p.place_player(t2.beater1.player_char, t2.beater1.row, t2.beater1.col)
        p.place_player(t1.beater2.player_char, t1.beater2.row, t1.beater2.col)
        p.place_player(t2.beater2.player_char, t2.beater2.row, t2.beater2.col)

    #Level 4:  both Seekers, Golden Snitch and 2 Beaters for each team as obstacles (Beaters do move)
    elif level == 4:
        snitch.col = 9
        snitch.row = 5
        p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)
        s1.row = 2
        s1.col = 2
        s2.row = 3
        s2.col = 2
        t1.beater1.row = 4
        t1.beater1.col = 3
        t2.beater1.row = 3
        t2.beater1.col = 3
        t1.beater2.row = 2
        t1.beater2.col = 3
        t2.beater2.row = 5
        t2.beater2.col = 3
        p.place_player(s1.player_char, s1.row, s1.col)
        p.place_player(s2.player_char, s2.row, s2.col)
        p.place_player(t1.beater1.player_char, t1.beater1.row, t1.beater1.col)
        p.place_player(t2.beater1.player_char, t2.beater1.row, t2.beater1.col)
        p.place_player(t1.beater2.player_char, t1.beater2.row, t1.beater2.col)
        p.place_player(t2.beater2.player_char, t2.beater2.row, t2.beater2.col)

    #Level 5:  both Seekers, Golden Snitch and all players from both teams in the field as obstacles (all objects do move)
    elif level == 5:
        snitch.col = 9
        snitch.row = 5
        p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)
        s1.row = 2
        s1.col = 2
        s2.row = 3
        s2.col = 2
        t1.beater1.row = 3
        t1.beater1.col = 14
        t2.beater1.row = 8
        t2.beater1.col = 4
        t1.beater2.row = 7
        t1.beater2.col = 7
        t2.beater2.row = 3
        t2.beater2.col = 6
        t1.keeper.row = 1
        t1.keeper.col = 9
        t2.keeper.row = 8
        t2.keeper.col = 8
        t1.chaser1.row = 10
        t1.chaser1.col = 5
        t1.chaser2.row = 3
        t1.chaser2.col = 8
        t1.chaser3.row = 11
        t1.chaser3.col = 7
        t2.chaser1.row = 12
        t2.chaser1.col = 15
        t2.chaser2.row = 8
        t2.chaser2.col = 10
        t2.chaser3.row = 1
        t2.chaser3.col = 10


        p.place_player(s1.player_char, s1.row, s1.col)
        p.place_player(s2.player_char, s2.row, s2.col)
        p.place_player(t1.beater1.player_char, t1.beater1.row, t1.beater1.col)
        p.place_player(t2.beater1.player_char, t2.beater1.row, t2.beater1.col)
        p.place_player(t1.beater2.player_char, t1.beater2.row, t1.beater2.col)
        p.place_player(t2.beater2.player_char, t2.beater2.row, t2.beater2.col)
        p.place_player(t1.keeper.player_char, t1.keeper.row, t1.keeper.col)
        p.place_player(t2.keeper.player_char, t2.keeper.row, t2.keeper.col)
        p.place_player(t1.chaser1.player_char, t1.chaser1.row, t1.chaser1.col)
        p.place_player(t1.chaser2.player_char, t1.chaser2.row, t1.chaser2.col)
        p.place_player(t1.chaser3.player_char, t1.chaser3.row, t1.chaser3.col)
        p.place_player(t2.chaser1.player_char, t2.chaser1.row, t2.chaser1.col)
        p.place_player(t2.chaser2.player_char, t2.chaser2.row, t2.chaser2.col)
        p.place_player(t2.chaser3.player_char, t2.chaser3.row, t2.chaser3.col)

#function to move the Snitch and other obstacles on the map (implements the fly function for Snitch and team members other than Seekers)
def update_pitch():
    if lvl._level > 0:
        if s1.snitch_caught is False and s2.snitch_caught is False:
            temp_row = snitch.row
            temp_col = snitch.col
            snitch.fly()
            if p.can_move(snitch.row, snitch.col):
                p.clear(temp_row, temp_col)
                p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)
            else:
                snitch.row = temp_row
                snitch.col = temp_col
            if lvl.level == 4:
                players = [t1.beater1, t1.beater2, t2.beater1, t2.beater2]
                for player in players:
                    temp_row = player.row
                    temp_col = player.col
                    player.fly()
                    if p.can_move(player.row, player.col) and player.row != s1.row and player.row != s2.row and player.col != s1.col and player.col != s2.col:
                        p.clear(temp_row, temp_col)
                        p.place_snitch(player.player_char, player.row, player.col)
                    else:
                        player.row = temp_row
                        player.col = temp_col

            elif lvl.level == 5:
                players = [t1.beater1, t1.beater2, t2.beater1, t2.beater2, t1.keeper, t2.keeper, t1.chaser1, t1.chaser2, t1.chaser3, t2.chaser1, t2.chaser2, t2.chaser3]
                for player in players:
                    temp_row = player.row
                    temp_col = player.col
                    player.fly()
                    if p.can_move(player.row, player.col) and player.row != s1.row and player.row != s2.row and player.col != s1.col and player.col != s2.col:
                        p.clear(temp_row, temp_col)
                        p.place_snitch(player.player_char, player.row, player.col)
                    else:
                        player.row = temp_row
                        player.col = temp_col

#method to move Seeker to the left / checks is the move valid
def fly_left(seeker):
    global snitch_caught
    global p
    global player1_moves
    global player2_moves
    seeker.fly('left')
    snitch_caught(seeker)
    if p.seeker_can_move(seeker.row, seeker.col) is True:
        col = seeker.col +1
        p.clear(seeker.row, col)
        p.place_player(seeker.player_char, seeker.row, seeker.col)
        if seeker == s1:
            player1_moves +=1
        else:
            player2_moves += 1
    else:
        seeker.col += 1

#method to move Seeker to the right / checks is the move valid
def fly_right(seeker):
    global snitch_caught
    global p
    global player1_moves
    global player2_moves
    seeker.fly('right')
    snitch_caught(seeker)
    if p.seeker_can_move(seeker.row, seeker.col) is True:
        col = seeker.col - 1
        p.clear(seeker.row, col)
        p.place_player(seeker.player_char, seeker.row, seeker.col)
        if seeker == s1:
            player1_moves +=1
        else:
            player2_moves += 1
    else:
        seeker.col -= 1

#method to move the Seeker up / checks is the move valid
def fly_up(seeker):
    global snitch_caught
    global p
    global player1_moves
    global player2_moves
    seeker.fly('up')
    snitch_caught(seeker)
    if p.seeker_can_move(seeker.row, seeker.col) is True:
        row = seeker.row +1
        p.clear(row, seeker.col)
        p.place_player(seeker.player_char, seeker.row, seeker.col)
        if seeker == s1:
            player1_moves +=1
        else:
            player2_moves += 1
    else:
        seeker.row += 1

#method to move the Seeker down / checks is the move valid
def fly_down(seeker):
    global snitch_caught
    global p
    global player1_moves
    global player2_moves
    seeker.fly('down')
    snitch_caught(seeker)
    if p.seeker_can_move(seeker.row, seeker.col) is True:
        row = seeker.row -1
        p.clear(row, seeker.col)
        p.place_player(seeker.player_char, seeker.row, seeker.col)
        if seeker == s1:
            player1_moves +=1
        else:
            player2_moves += 1
    else:
        seeker.row -= 1

#create objects from Game, Level and Pitch classes
game = Game()
lvl = Level()
p = Pitch(lvl.level)

#create the first obcject from the team class, assign player char to each team member
t1 = Team("Gryffindor")
t1.seeker.player_name = "Harry"
t1.seeker.player_char = "$"
t1.chaser1.player_char = "1"
t1.chaser2.player_char = "1"
t1.chaser3.player_char = '1'
t1.beater1.player_char = '1'
t1.beater2.player_char = '1'
t1.keeper.player_char = '1'

#create the second obcject from the team class, assign player char to each team member
t2 = Team("Slytherin")
t2.seeker.player_name = "Terence"
t2.seeker.player_char = "9"
t2.chaser1.player_char = "2"
t2.chaser2.player_char = "2"
t2.chaser3.player_char = '2'
t2.beater1.player_char = '2'
t2.beater2.player_char = '2'
t2.keeper.player_char = '2'

#create variables for teams seekers for easier use
s1 = t1.seeker
s2 = t2.seeker

#create an obcject from the Snitch class
snitch = Snitch()

#place players and snitch in the pitch / starting positions
p.place_player(s1.player_char, s1.row, s1.col)
s2.row = 2
s2.col = 12
p.place_player(t2.seeker.player_char, t2.seeker.row, t2.seeker.col)
p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)

#set level to 1 and player moves to 0
level = 1
player1_moves = 0
player2_moves = 0

#main program
def main():

    global fps_clock, screen, img_dict, tile_mapping, font, p, level, w_font, bold_txt, player1_moves, player2_moves


    #draw the tile sprites onto this surface.
    #this creates the visual map
    def draw_map(pitch):
        map_width = pitch.get_width() * tile_width
        map_height = pitch.get_height() * tile_height
        map_surf = pygame.Surface((map_width, map_height))
        map_surf.fill(bg_color)
        for h in range(pitch.get_height()):
            for w in range(pitch.get_width()):
                this_tile = pygame.Rect((w * tile_width, h * tile_floor_height, tile_width, tile_height))
                if pitch.get_char_at_pos(h, w) in tile_mapping:
                    #checks in the TILEMAPPING directory above to see if there is a
                    #matching picture, then renders it
                    base_tile = tile_mapping[pitch.get_char_at_pos(h,w)]
                # Draw the tiles for the map.
                map_surf.blit(base_tile, this_tile)
        return map_surf

    #shutdown routine
    def terminate():
        global finished
        finished = True
        pygame.quit()
        sys.exit()

    #display teams scores on the screen
    def score_board():
        t1_score_text = font.render(t1.team_name + ": " + str(t1.team_score), 1, red_txt)
        t2_score_text = font.render(t2.team_name + ": " + str(t2.team_score), 1, blue_txt)
        screen.blit(t1_score_text, (30, 70))
        screen.blit(t2_score_text, (475, 70))

    #display the level on the screen
    def level_txt():
        lvl_txt = font.render("Level: " + str(lvl.level), 1, black_txt)
        screen.blit(lvl_txt, ((half_width - 15), 20))

    #displays the winning team on the screen
    def winner_txt():
        winner = game.winner
        winner = winner.upper()
        winner_txt = w_font.render(winner + " WINS!", 1, white_txt)
        screen.blit(winner_txt, ((half_width-140), (half_height-50)))

    #displays the number of players moves on the screen
    def players_moves_txt():
        player1_moves_txt = small_font.render("player_1 moves: " + str(player1_moves), 1, black_txt)
        screen.blit(player1_moves_txt, (28, 580))
        player2_moves_txt = small_font.render("player_2 moves: " + str(player2_moves), 1, black_txt)
        screen.blit(player2_moves_txt, (495, 580))

    #main game loop allowing to restart the game after it was finished
    restart = 1
    while restart ==1:
        screen.fill(bg_color)
        map_surf = draw_map(p)
        map_surf_rect = map_surf.get_rect()
        map_surf_rect.center = (half_width, half_height)
        screen.blit(map_surf, map_surf_rect)
        finished = False

        #game loop, itterates until the single game is finished / takes users input to move the seekers on the map
        #error handling if the input is not valid
        while finished == False:
            while s1.snitch_caught is False and s2.snitch_caught is False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == KEYDOWN:
                        if event.key == K_d:
                            fly_right(s1)
                            update_pitch()
                        elif event.key == K_s:
                            fly_down(s1)
                            update_pitch()
                        elif event.key == K_w:
                            fly_up(s1)
                            update_pitch()
                        elif event.key == K_a:
                            fly_left(s1)
                            update_pitch()
                        elif event.key == K_l:
                            fly_right(s2)
                            update_pitch()
                        elif event.key == K_k:
                            fly_down(s2)
                            update_pitch()
                        elif event.key == K_i:
                            fly_up(s2)
                            update_pitch()
                        elif event.key == K_j:
                            fly_left(s2)
                            update_pitch()
                        # elif event.key == K_SPACE:
                        #     restart()
                        else:
                            print("Wrong input")
                            print("Use keys: a, s, w, d to navigate player 1 (red)")
                            print("Use keys: j,i,k,l to navigate player 2 (blue)")

                #fill the screen with the background color
                screen.fill(bg_color)
                #call the draw_map function and update the screen with each iteration
                map_surf = draw_map(p)
                map_surf_rect = map_surf.get_rect()
                map_surf_rect.center = (half_width, half_height)
                screen.blit(map_surf, map_surf_rect)

                #update the score_board
                score_board()
                #update the playes_moves
                players_moves_txt()
                #update the level
                level_txt()
                pygame.display.update()
                #clock tick
                fps_clock.tick()

            #if level finished and not the last level, load the next level
            if lvl.level < lvl.is_last:
                level += 1
                p = Pitch(lvl.level)
                load_level(level)
                lvl.increase_level()
                screen.fill(bg_color)
                map_surf = draw_map(p)

                map_surf_rect = map_surf.get_rect()
                map_surf_rect.center = (half_width, half_height)
                screen.blit(map_surf, map_surf_rect)

                pygame.display.update() # draw DISPLAYSURF to the screen.
                fps_clock.tick()

            #if last level finished, update the team scores and display the winner on the screen and set finished to true
            else:
                game.team1_score = t1.team_score
                game.team2_score = t2.team_score
                if game.team1_score > game.team2_score:
                    game.winner = t1.team_name
                else:
                    game.winner = t2.team_name
                print(t1.team_name + " score: " + str(game.team1_score) + " points")
                print(t2.team_name + " score: " + str(game.team2_score) + " points")
                print(game.winner_string())

                #display the txt to inform the player how to restart the game
                restart_txt = bold_txt.render("Press space to restart", 1, (0, 0, 0))
                screen.blit(restart_txt, ((half_width - 70), 60))
                map_surf_rect = map_surf.get_rect()
                map_surf_rect.center = (half_width, half_height)
                screen.blit(map_surf, map_surf_rect)

                winner_txt()
                pygame.display.update()
                fps_clock.tick()
                finished = True

        #while the game has been finished, if the player chooses to close the game, terminate the program
        #if the player presses the space bar, set all scores to 0 and reinitialize level 1 to play again
        while finished is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                    restart = 0
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        finished = False
                        restart = 1
                        player1_moves = 0
                        player2_moves = 0
                        t1.team_score = 0
                        t2.team_score = 0
                        s1.snitch_caught = False
                        s2.snitch_caught = False
                        lvl.level = 1
                        level = 1
                        p = Pitch(lvl.level)
                        s1.row = 2
                        s1.col = 2
                        p.place_player(s1.player_char, t1.seeker.row, t1.seeker.col)
                        s2.row = 2
                        s2.col = 12
                        p.place_player(t2.seeker.player_char, t2.seeker.row, t2.seeker.col)
                        p.place_snitch(snitch.snitch_char, snitch.row, snitch.col)

                    else:
                        pass
                else:
                    pass




if __name__ == '__main__':
    main()
