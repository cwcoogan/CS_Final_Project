"""
Chase Coogan
Fall 2022
CS 5001
functions.py
"""

import pickle
from functools import partial
from Tile import *
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
        """
        Method -- __init__

        Parameter -- self

        Returns -- turtle screen, screen size, initial object of the puzzle
        """
        
        self.screen = turtle.Screen()
        self.screen.setup(800, 730)
        self.puzzle = Puzzle("slider_puzzle_project_fall2021_assets-2022/mario.puz")
        self.count = 0
        
    def begin_game(self):
        """
        Method -- begin_game

        Parameter -- self

        Returns -- set splash screen, leaderboards, quit/load/reset
                   buttons, and keeps and updates the score.
        """
        self.splash_screen()
        self.update_leaders()
        self.user_input()
        self.draw_rectangles()
        self.quit_button()
        self.load_button()
        self.reset_button() 
        self.leaderboard() 
        self.keep_score()
    
    def reload(self):
        """
        Method -- reload

        Parameter -- self

        Returns -- helper function to restart the puzzle
                   game and get the path
        """
        self.load_puzzle(self.puzzle.get_path())
    
    def draw_rectangles(self):
        """
        Method -- draw_rectangles()

        Parameter -- self

        Returns -- Creates the rectangle objects that the puzzles
                   will be displayed in
        """
        # leaderboard
        rectangle1 = RectangleDimensions(175, 392, 120, -150, "blue")
        rectangle1.go_to()
        rectangle1.draw()

        # tile square
        rectangle2 = RectangleDimensions(450, 392, -350, -150, "black")
        rectangle2.go_to()
        rectangle2.draw()

        # reset/load box
        rectangle3 = RectangleDimensions(650, 100, -350,-300, "black")
        rectangle3.go_to()
        rectangle3.draw()

    def splash_screen(self):
        """
        Method -- splash_screen

        Parameters - None
        
        Returns - Sets splash screen image and timer
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif"
        splash = Tile(0, 0, path, self.screen)
        splash.display_img()
        time.sleep(3)
        splash.t.hideturtle()
        
    def user_input(self):
        """
        Method -- user_input()

        Patameters - self

        Returns - users name and the total # of attempts
                between 5 - 200 to play the game
        """
        self.name = turtle.textinput("CS5001 Puzzle Slide", "Your Name: ")
        self.num_moves = int(turtle.numinput("CS5001 Puzzle Slide - Moves", "Enter the number of moves (chances) you want (5-200)?", 20, 5, 200))
        
    def quit_img(self, x, y):
        """ 
        Method -- quit_img

        Parameters -- self, x, y

        Returns -- displays the quit_img when the user
                   clicks on the quit button
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/quitmsg.gif"
        get_quit_img = Tile(0, 0, path, self.screen)
        get_quit_img.display_img()    
        time.sleep(3)
        self.screen.bye()
    
    def lose(self):
        """
        Method -- lose

        Parameter -- self

        Returns -- displays the lose image when the user loses
                   the game
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/Lose.gif"
        t = Tile(0, 0, path, self.screen)
        t.display_img()    
        time.sleep(3)
        self.screen.bye()
        
    def quit_button(self):
        """
        Method -- quit_button

        Parameters -- self

        Returns --  displays the button and allows users to
                    click on it. Saves the leaderboard when quit
        """
        self.save_leaders()
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif"
        exit = Tile(250, -250, path, self.screen)
        exit.display_img()
        exit.t.onclick(self.quit_img)

    def select_puzzle(self, x, y):
        """
        Method -- select_puzzle

        Parameters -- self, x, y

        Returns -- allows the user to select the choice
                   of what puzzle to load. Then clears the current
                   puzzle and begins to load the new puzzle.
        """
        selection = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish to load. Choice are:\n\nluigi.puz:\nsmiley.puz\nfifteen.puz\nyoshi.puz\nmario.puz\nmalformed_mario.puz\ncookie.puz\n")
        path = "slider_puzzle_project_fall2021_assets-2022/" + selection

        self.puzzle.clear()

        self.puzzle = Puzzle(path)
        
        self.load_puzzle(self.puzzle.get_path())
          
    def after_error(self):
        """
        Method -- after_error

        Parameter -- self

        Returns -- After getting an error message, this
                   helper function will reload the game
        """
        selection = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish to load.\n" 
        "Choice are:\n\nluigi.puz:\nsmiley.puz\nfifteen.puz\nyoshi.puz\nmario.puz\nmalformed_mario.puz\n")
        path = "slider_puzzle_project_fall2021_assets-2022/" + selection
        self.puzzle = Puzzle(path)
        self.load_puzzle(self.puzzle.get_path())
           
    def load_button(self):
        """
        Method -- load_button

        Parameter -- self

        Returns -- creates the load button as an object and displays
                   the image. Allows users to click on the load button.
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif"
        load = Tile(150, -250, path, self.screen)
        load.display_img()
        load.t.onclick(self.select_puzzle)
        
    def reset_button(self):
        """
        Method -- reset_button

        Parameter -- self

        Returns -- displays the reset button & allows 
                   users the reset the puzzle to the 
                   correct image format by clicking reset.
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif"
        reset = Tile(50, -250, path, self.screen)
        reset.display_img()
        reset.t.onclick(self.reset_puzzle) 

    def reset_puzzle(self, x, y):
        """
        Method -- reset_puzzle

        Parameter -- self, x, y

        Returns -- Puzzle object in the winning format
        """
        self.puzzle = Puzzle(self.puzzle.get_path())
        self.load_puzzle(self.puzzle.get_path(), scrambled=False)

    def leaderboard_img(self, thumbnail):
        """
        Method -- leaderboard_img

        Parameter -- self, thumbnail

        Returns -- Thumbnail object that allows us to change
                    the thumbnail to the puzzles correct thumbnail
                    and display it.
        """
        thumb = Tile(250, 220, thumbnail, self.screen)
        thumb.display_img()
        self.puzzle.set_thumbnail(thumb)
        
    def leaderboard(self):
        """
        Method -- leaderboard

        Parameter -- self

        Returns -- leaderboard object with the leaderboard text,
                   font, and color.
        """
        leader = Tile(130, 215, img_file=None, screen=self.screen)
        leader.t.color('blue')
        leader.display_text("Leaders: ", 15)
        
        leader.t.hideturtle()
        self.display_leaders()
        
    def display_leaders(self):
        """
        Method -- display_leaders

        Parameter -- self

        Returns -- Turtle object that displays the leaderboards
                   names of those who have won the game. 
        """
        names = Tile(130, 150, img_file= None, screen=self.screen)
        for each in self.leaderboard_name:
            names.display_text(f'{each} : {self.leaderboard_name[each]}', 15)  
            names.y -= 20
            names.t.hideturtle()

    def keep_score(self):
        """
        Method -- keep_score()

        Parameters - self

        Returns -- Keeps score of the players moves
        against the counter and will either win or
        lose the game based on this condition
        """
        if self.count == self.num_moves:
            return True
        
        self.score = Tile(-320, -260, img_file=None, screen=self.screen)
        self.score.t.color('blue')
        self.score.display_text(f'Player Moves: {self.count}', 20)
        self.score.t.hideturtle()

        return False
    
    def error(self):
        """
        Method -- error

        Parameter - self

        Returns -- displays the file error image and calls the
                   after_error method
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/file_error.gif"
        t = Tile(0, 0, path, self.screen)
        t.display_img()    
        time.sleep(1)
        t.t.hideturtle()
        self.after_error()

    def load_puzzle(self, p, scrambled=True):
        """
        Method -- load_puzzle

        Parameter -- self, p, scrambled=True

        Returns -- The main puzzle logic resides here that will
                   display the puzzle image showcasing the puzzle 
                   image that the user has loaded into the game. 

                   Default value is scrambled, meaning that every 
                   puzzle that is loaded will begin as shuffled.
        """
        lst = get_puzzle(p) 

        if not lst:
            self.error()

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
        """
        Method -- check_click

        Parameter -- self, clicked_tile, x, y

        Returns -- Logic that checks if the user has selected
                   a blank tile and then checks for the surrounding
                   neighbors where it can be swapped with.

                   Checks if the user is out of moves and loses or wins
                   the game
        """
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

    def leader_error(self):
        """
        Method -- leader_error

        Parameter - self

        Returns -- leaderboard error pops up if no
                   leaderboard file is built
        """
        path = "slider_puzzle_project_fall2021_assets-2022/Resources/leaderboard_error.gif"
        t = Tile(0, 0, path, self.screen)
        t.display_img()    
        time.sleep(2)
        turtle.bye()
        
    def check_win(self):
        """
        Method -- check_win

        Paramter -- self

        Returns -- True boolean value if the list
                   is equal to the sorted list.
        """
        lst = []
        for row in self.puzzle.tiles:
            for tile in row:
                lst.append(tile.count)

        if lst == sorted(lst):
            return True
            
    def win(self):
        """
        Method -- win

        Parameter -- self

        Returns -- displays the winning image if the user has 
                   won the game, and then displays the credits image.

                   If the user wins, their name and moves will be added to
                   the leaderboards.
        """
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
        """
        Method -- get_blank_tile

        Paramter -- self

        Returns -- iterates through the puzzle tiles object
                   and returns True if the tile is blank
        """
        for row in self.puzzle.tiles:
            for tile in row:
                if tile.blank:
                    return tile

    def add_leader(self, moves):
        """
        Method -- add_leader

        Parameter -- self, moves

        Returns -- adds user to the leaderboard along
                   with their moves and saves it
        """
        self.leaderboard_name[moves] = self.name
        self.save_leaders()

    def save_leaders(self):
        """
        Method -- save_leaders

        Parameter -- self

        Returns -- Stores the leaderboard data in a file
                   named 'leaderboards.data'
        """
        newFile = 'leaderboards.data'
        with open(newFile, 'wb') as f:
            pickle.dump(self.leaderboard_name, f)

    def update_leaders(self):
        """
        Method -- update_leaders

        Paramter -- self

        Returns -- loads & reads the data from the 'leaderboards.data'
                   file. 
                   
                   Raises an error if the file is not found.
        """
        newFile = 'leaderboards.data' 
        try:
            with open(newFile, 'rb') as f:
                self.leaderboard_name = pickle.load(f)
        except FileNotFoundError:
            self.leader_error()

