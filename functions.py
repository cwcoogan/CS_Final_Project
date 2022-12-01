"""
Chase Coogan
Fall 2022
CS 5001
functions.py
"""

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
from pprint import pprint
import math

screen = turtle.Screen()
screen.setup(800, 730)

puzzle = Puzzle("slider_puzzle_project_fall2021_assets-2022/mario.puz")

def splash_screen():
    """
    Function splash_screen

    Parameters - None
    
    Returns - None. Sets splash screen image 
              and timer
    """
    path = "slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif"
    splash = Tile(0, 0, path, screen)
    splash.display_img()
    time.sleep(3)
    splash.t.hideturtle()
    
def user_input():
    """
    FUNCTION -- user_input()

    Patameters - None

    Returns - users name and the total # of attempts
              between 5 - 200 to play the game
    """
    name = turtle.textinput("CS5001 Puzzle Slide", "Your Name: ")
    num_moves = int(turtle.numinput("CS5001 Puzzle Slide - Moves", "Enter the number of moves (chances) you want (5-200)?"))
    
    # checks to see if the number of chances is within the range of 5-200
    while num_moves < 5 or num_moves > 200:
        num_moves = int(turtle.numinput("CS5001 Puzzle Slide - Moves", "Enter the number of moves (chances) you want (5-200)?"))   
    

def quit_img(x, y):
    path = "slider_puzzle_project_fall2021_assets-2022/Resources/quitmsg.gif"
    get_quit_img = Tile(0, 0, path, screen)
    get_quit_img.display_img()    
    time.sleep(3)
    screen.bye()
    
def quit_button():
    path = "slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif"
    exit = Tile(250, -250, path, screen)
    exit.display_img()
    exit.t.onclick(quit_img)

def select_puzzle(x, y):
    global puzzle
    selection = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish to load. Choice are:\n\nluigi.puz:\nsmiley.puz\nfifteen.puz\nyoshi.puz\nmario.puz\n")
    path = "slider_puzzle_project_fall2021_assets-2022/" + selection
    
    puzzle.clear()

    puzzle = Puzzle(path)

    load_puzzle(puzzle.get_path())

def load_button():
    path = "slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif"
    load = Tile(150, -250, path, screen)
    load.display_img()
    load.t.onclick(select_puzzle)
    
def reset_button():
    path = "slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif"
    reset = Tile(50, -250, path, screen)
    reset.display_img()
    reset.t.onclick(reset_puzzle) 

def reset_puzzle(x, y):
    global puzzle
    puzzle = Puzzle(puzzle.get_path())
    load_puzzle(puzzle.get_path(), scrambled=False)

def leaderboard_img(thumbnail):
    thumb = Tile(250, 220, thumbnail, screen)
    thumb.display_img()
    puzzle.set_thumbnail(thumb)
    
def leaderboard():
    leader = Tile(130, 215, img_file=None, screen=screen)
    leader.t.color('blue')
    leader.display_text("Leaders: ", 15)
    leader.t.hideturtle()

def keep_score():
    """
    FUNCTION -- keep_score()

    Parameters - None.

    Returns - the players score. Displays either
    "win" or "lose" depending on if player wins
    or loses.
    """
    count = 0
    score = Tile(-320, -260, img_file=None, screen=screen)
    score.t.color('blue')
    score.display_text('Player Moves: 0', 20)
    score.t.hideturtle()
    
def load_puzzle(p=puzzle.get_path(), scrambled=True):
    lst = get_puzzle(p)

    
    x = -286.5
    y = 191
    
    unshuffled_list, number, shuffle_list, thumbnail = lst 

    thumbnail = "slider_puzzle_project_fall2021_assets-2022/" + thumbnail
    leaderboard_img(thumbnail)
    
    placed_tiles = 0
    tiles_in_line = floor(sqrt(number))

    if scrambled:
        images = shuffle_list
    else:
        images = unshuffled_list

    

    rows = int(math.sqrt(number))
    count = 0 
    for i in range(rows):
        puzzle.tiles.append([])
        for j in range(rows):
            path = "slider_puzzle_project_fall2021_assets-2022/" + images[count]
            t = Tile(x, y, path, screen, (i, j))
            puzzle.tiles[i].append(t)
            t.display_img()
            count += 1

            x = x + 112.5
        
        x = -286.5
        y -= 98


    for row in puzzle.tiles:
        for tile in row:
            tile.t.onclick(partial(check_click, tile))

def check_click(clicked_tile, x, y):
    
    blank_tile = get_blank_tile()
    bx, by = blank_tile.location
    blank_neighbors = [(bx + 1, by), (bx - 1, by), (bx, by + 1), (bx, by - 1)] 
    
    if clicked_tile.location in blank_neighbors:
        puzzle.swap_tiles(clicked_tile, blank_tile)
        check_win()
    else:
        print("SWAPNIL NO SWAPPING")

# Neeely is broken here
def check_win():
    lst = []
    for row in puzzle.tiles:
        for tile in row:
            lst.append(tile.img_file[-6:-4].strip("/"))
    
    lst.remove("nk")
    print(lst)

    if lst == sorted(lst, reverse=True):
        print("WINERRRRRRRR")


def get_blank_tile():
    for row in puzzle.tiles:
        for tile in row:
            if tile.blank:
                return tile