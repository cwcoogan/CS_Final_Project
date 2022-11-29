"""
Chase Coogan
Fall 2022
CS 5001
functions.py
"""

from draw_rectangle import *
from RectangleDimensions import *
from math import *
from generate_puzzle import *
import turtle
import time
import random


screen = turtle.Screen()
screen.setup(800, 730)

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
    selection = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish to load. Choice are:\n\nluigi.puz:\nsmiley.puz\nfifteen.puz\nyoshi.puz\nmario.puz\n")
    path = "slider_puzzle_project_fall2021_assets-2022/" + selection
    load_puzzle(path)

def load_button():
    t3 = turtle.Turtle()
    t3.speed("fastest")
    t3.penup()
    screen.addshape("slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif")
    t3.goto(150, -250)
    t3.pendown()
    t3.shape("slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif")
    t3.onclick(select_puzzle)
    
def reset_button():
    t4 = turtle.Turtle()
    t4.speed("fastest")
    t4.penup()
    screen.addshape("slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif")
    t4.goto(50, -250)
    t4.pendown()
    t4.shape("slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif")
    # t4.onclick(p) # needs to make this work
    
def leaderboard_img(thumbnail):
    t5 = turtle.Turtle()
    t5.speed("fastest")
    t5.penup()
    screen.addshape(thumbnail)
    t5.goto(250, 220)
    t5.pendown()
    t5.shape(thumbnail)
    
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


def load_puzzle(p):
    lst = get_puzzle(p)
    x = -286.5
    y = 191
    count = 0
    img_list, number, shuffle_list, thumbnail = lst 
    thumbnail = "slider_puzzle_project_fall2021_assets-2022/" + thumbnail
    leaderboard_img(thumbnail)
    sq_rt = floor(sqrt(number))
    for path in shuffle_list: # if I change this to img_list it will be the good puzzle
        t8 = turtle.Turtle()
        t8.speed("fastest")
        t8.penup()
        t8.goto(x, y)
        t8.pendown()
        path = "slider_puzzle_project_fall2021_assets-2022/" + path
        screen.addshape(path)
        t8.shape(path)
        count += 1
        if x <= 50 and count < sq_rt:
            x = x + 112.5
        else:
            x = -286.5
            y = y - 98
            count = 0 


# def click_change():
#     t99 = turtle.Turtle()
#     t99.onclick(reset_button)
#     if t99.onclick(load_button) == reset_button():
#         load_good_puzzle("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/mario.puz")

# def load_good_puzzle(p):
#     lst = get_puzzle(p)
#     x = -286.5
#     y = 191
#     count = 0
#     img_list, number, shuffle_list, thumbnail = lst 
#     thumbnail = "slider_puzzle_project_fall2021_assets-2022/" + thumbnail
#     leaderboard_img(thumbnail)
#     sq_rt = floor(sqrt(number))
#     for path in img_list: # if I change this to img_list it will be the good puzzle
#         t8 = turtle.Turtle()
#         t8.speed("fastest")
#         t8.penup()
#         t8.goto(x, y)
#         t8.pendown()
#         path = "slider_puzzle_project_fall2021_assets-2022/" + path
#         screen.addshape(path)
#         t8.shape(path)
#         count += 1
#         if x <= 50 and count < sq_rt:
#             x = x + 112.5
#         else:
#             x = -286.5
#             y = y - 98
#             count = 0 