"""
Chase Coogan
Fall 2022
CS 5001
functions.py
"""

import pickle
from functools import partial
from Tile import *
from draw_rectangle import *
from RectangleDimensions import *
from math import *
from generate_puzzle import *
import turtle
import time
import random
from Puzzle import Puzzle
import math

class PuzzleRunner:
    def __init__(self):
        
        self.screen = turtle.Screen()
        self.screen.setup(800, 730)
        self.puzzle = Puzzle("slider_puzzle_project_fall2021_assets-2022/mario.puz")
        self.leaderboard_name = {}
        self.count = 0

    def splash_screen(self):
        """
        Function splash_screen

        Parameters - None
        
        Returns - None. Sets splash screen image 
                and timer
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif"
        splash = Tile(0, 0, path, self.screen)
        splash.display_img()
        time.sleep(3)
        splash.t.hideturtle()
        
    def user_input(self):
        """
        FUNCTION -- user_input()

        Patameters - None

        Returns - users name and the total # of attempts
                between 5 - 200 to play the game
        """
        self.name = turtle.textinput("CS5001 Puzzle Slide", "Your Name: ")
        self.num_moves = int(turtle.numinput("CS5001 Puzzle Slide - Moves", "Enter the number of moves (chances) you want (5-200)?", 20, 5, 200))
        
    def quit_img(self, x, y):
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/quitmsg.gif"
        get_quit_img = Tile(0, 0, path, self.screen)
        get_quit_img.display_img()    
        time.sleep(3)
        self.screen.bye()
    
    def lose(self):
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/Lose.gif"
        t = Tile(0, 0, path, self.screen)
        t.display_img()    
        time.sleep(3)
        self.screen.bye()
        
    def quit_button(self):
        self.save_leaders()
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif"
        exit = Tile(250, -250, path, self.screen)
        exit.display_img()
        exit.t.onclick(self.quit_img)
        
    def get_error_img(self):
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/file_error.gif"
        error_img = Tile(0, 0, path, screen=self.screen)
        error_img.display_img()
        
    def select_puzzle(self, x, y):
        selection = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish to load. Choice are:\n\nluigi.puz:\nsmiley.puz\nfifteen.puz\nyoshi.puz\nmario.puz\n")
        path = "slider_puzzle_project_fall2021_assets-2022/" + selection
        
        # display error image if path not found
        if selection.lower() != "mario.puz" and \
        selection.lower() != "yoshi.puz" and \
        selection.lower() != "fifteen.puz" and \
        selection.lower() != "smiley.puz" and \
        selection.lower() != "luigi.puz": 
            self.get_error_img()

        self.puzzle.clear()

        self.puzzle = Puzzle(path)

        self.load_puzzle(self.puzzle.get_path())
           
    def load_button(self):
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif"
        load = Tile(150, -250, path, self.screen)
        load.display_img()
        load.t.onclick(self.select_puzzle)
        
    def reset_button(self):
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif"
        reset = Tile(50, -250, path, self.screen)
        reset.display_img()
        reset.t.onclick(self.reset_puzzle) 

    def reset_puzzle(self, x, y):
        self.puzzle = Puzzle(self.puzzle.get_path())
        self.load_puzzle(self.puzzle.get_path(), scrambled=False)

    def leaderboard_img(self, thumbnail):
        thumb = Tile(250, 220, thumbnail, self.screen)
        thumb.display_img()
        self.puzzle.set_thumbnail(thumb)
        
    def leaderboard(self):
        leader = Tile(130, 215, img_file=None, screen=self.screen)
        leader.t.color('blue')
        leader.display_text("Leaders: ", 15)
        
        leader.t.hideturtle()
        self.display_leaders()
        
    def display_leaders(self):
        
        print(self.leaderboard_name)
        names = Tile(130, 175, img_file= None, screen=self.screen)
        for each in self.leaderboard_name:
            names.display_text(f'{each} : {self.leaderboard_name[each]}', 15)  
            names.y -= 20
            names.t.hideturtle()

    def keep_score(self):
        """
        FUNCTION -- keep_score()

        Parameters - None.

        Returns - the players score. Displays either
        "win" or "lose" depending on if player wins
        or loses.
        """
        if self.count == self.num_moves:
            return True
        
        self.score = Tile(-320, -260, img_file=None, screen=self.screen)
        self.score.t.color('blue')
        self.score.display_text(f'Player Moves: {self.count}', 20)
        self.score.t.hideturtle()

        return False

    def load_puzzle(self, p, scrambled=True):
        lst = get_puzzle(p)

        x = -286.5
        y = 191
        
        unshuffled_list, number, shuffle_list, thumbnail = lst 

        thumbnail = "slider_puzzle_project_fall2021_assets-2022/" + thumbnail
        self.leaderboard_img(thumbnail)
        
        if scrambled:
            images = shuffle_list
        else:
            images = unshuffled_list
            
        rows = int(math.sqrt(number))
        count = 0 
        for i in range(rows):
            self.puzzle.tiles.append([])
            for j in range(rows):
                img = images[count]
                path = "slider_puzzle_project_fall2021_assets-2022/" + img
                t = Tile(x, y, path, self.screen, (i, j), count=unshuffled_list.index(img))
                self.puzzle.tiles[i].append(t)
                t.display_img()
                count += 1

                x = x + 112.5
            
            x = -286.5
            y -= 98


        for row in self.puzzle.tiles:
            for tile in row:
                tile.t.onclick(partial(self.check_click, tile))

    def check_click(self, clicked_tile, x, y):
        # should I check clicks here?  
        count = 0

        blank_tile = self.get_blank_tile()
        bx, by = blank_tile.location
        blank_neighbors = [(bx + 1, by), (bx - 1, by), (bx, by + 1), (bx, by - 1)] 
        if clicked_tile.location in blank_neighbors:
            self.puzzle.swap_tiles(clicked_tile, blank_tile)
            self.score.t.clear()
            self.count += 1
            no_moves = self.keep_score()
            if no_moves and not self.check_win():
                self.lose()
                
            win = self.check_win()
            if win:
                self.win()

    def check_win(self):
        lst = []
        for row in self.puzzle.tiles:
            for tile in row:
                lst.append(tile.count)

        print(lst)
        print(sorted(lst))
        if lst == sorted(lst):
            return True
            
    def win(self):
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/winner.gif"
        path_2 = "slider_puzzle_project_fall2021_assets-2022/Resources/credits.gif"
        winner = Tile(0,0, path, screen=self.screen)
        winner2 = Tile(0,0, path_2, screen=self.screen)
        self.add_leader(self.num_moves)
        winner.display_img()
        time.sleep(1)
        winner.t.clear()
        winner2.display_img()
        time.sleep(2)
        self.screen.bye()

    def get_blank_tile(self):
        for row in self.puzzle.tiles:
            for tile in row:
                if tile.blank:
                    return tile

    def add_leader(self, moves):
        self.leaderboard_name[moves] = self.name
        self.save_leaders()

    # Store Data
    def save_leaders(self):
        newFile = 'leaderboards.data'
        with open(newFile, 'wb') as f:
            pickle.dump(self.leaderboard_name, f)

    # Read Data 
    def update_leaders(self):
        newFile = 'leaderboards.data' 
        with open(newFile, 'rb') as f:
            self.leaderboard_name = pickle.load(f)

