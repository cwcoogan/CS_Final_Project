"""
Chase Coogan
Fall 2022
CS 5001
functions.py
"""

from Tile import *
from draw_rectangle import *
from RectangleDimensions import *
from math import *
from generate_puzzle import *
import turtle
import time
import random
from Puzzle import Puzzle

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
    turtle.hideturtle()
    t1 = turtle.Turtle()
    t1.speed("fastest")
    screen.addshape("slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif")
    t1.shape("slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif")
    t = 3
    time.sleep(t)
    t1.hideturtle()
    
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
    t9 = turtle.Turtle()
    t9.speed("fastest")
    img = screen.addshape("slider_puzzle_project_fall2021_assets-2022/Resources/quitmsg.gif")
    t9.shape("slider_puzzle_project_fall2021_assets-2022/Resources/quitmsg.gif")
    time.sleep(3)
    screen.bye()
    
def quit_button():
    t2 = turtle.Turtle()
    t2.speed("fastest")
    t2.penup()
    screen.addshape("slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif")
    t2.goto(250, -250)
    t2.pendown()
    t2.shape("slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif")
    t2.onclick(quit_img)

def select_puzzle(x, y):
    global puzzle
    selection = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish to load. Choice are:\n\nluigi.puz:\nsmiley.puz\nfifteen.puz\nyoshi.puz\nmario.puz\n")
    path = "slider_puzzle_project_fall2021_assets-2022/" + selection
    
    for tile in puzzle.tiles:
        tile.t.hideturtle()
    
    puzzle.get_thumbnail().t.hideturtle()

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
    load_puzzle(puzzle.get_path(),scrambled=False)

def leaderboard_img(thumbnail):
    thumb = Tile(250, 220, thumbnail, screen)
    thumb.display_img()
    puzzle.set_thumbnail(thumb)
    
def leaderboard():
    t6 = turtle.Turtle()
    t6.speed("fastest")
    t6.penup()
    t6.goto(130, 215)
    t6.pendown()
    t6.color("blue")
    t6.write("Leaders: ", font=("Ariel", 15, "normal"))
    t6.hideturtle()

def keep_score():
    """
    FUNCTION -- keep_score()

    Parameters - None.

    Returns - the players score. Displays either
    "win" or "lose" depending on if player wins
    or loses.
    """
    count = 0
    t7 = turtle.Turtle()
    t7.speed("fastest")
    t7.penup()
    t7.goto(-320, -260)
    t7.pendown()
    t7.color('blue')
    t7.write('Player Attempts: 0', font=("Ariel", 20, "normal"))
    t7.hideturtle()
    # need to iterate through count and display the total number based
    # on clicks.. 
    # cant build this fully until the click function is built.

    
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

    for path in images:
        
        path = "slider_puzzle_project_fall2021_assets-2022/" + path
        t = Tile(x, y, path, screen)
        t.set_puzzle(path)
        t.display_img()
        puzzle.tiles.append(t)

        placed_tiles += 1
        if x <= 50 and placed_tiles < tiles_in_line:
            x = x + 112.5
        
        else:
            x = -286.5
            y = y - 98
            placed_tiles = 0 
    print(puzzle.tiles)