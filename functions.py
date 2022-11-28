"""
Chase Coogan
Fall 2022
CS 5001
helper file storing classes and functions
for the puzzle game.
"""

from GeneratePuzzle import *
import turtle
import time
import random

screen = turtle.Screen()
screen.setup(800, 730)


def splash_screen():
    """
    Function splash_screen

    initializes the splash screen and sets it to appear 
    for 3 total seconds and then it goes away
    """
    turtle.hideturtle()
    t1 = turtle.Turtle()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif")
    t1.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/splash_screen.gif")
    t = 3
    time.sleep(t)
    t1.hideturtle()
    
def user_input():
    """
    FUNCTION -- user_input()

    this function gets the users name and the total number
    of chances they want between 5-200. 
    """
    name = turtle.textinput("CS5001 Puzzle Slide", "Your Name: ")
    num_moves = int(turtle.numinput("CS5001 Puzzle Slide - Moves", "Enter the number of moves (chances) you want (5-200)?"))

    # checks to see if the number of chances is within the range of 5-200
    while num_moves < 5 or num_moves > 200:
        num_moves = int(turtle.numinput("CS5001 Puzzle Slide - Moves", "Enter the number of moves (chances) you want (5-200)?"))   
    
    
class RectangleDimensions:
    """
    Class - RectangleDimensions

    this class takes the length, width, coordinates and color
    to create a rectangle. This will be used to configure the 
    gameboard.
    """
    def __init__(self, length, width, x_coord, y_coord, color):
        self.length = length
        self.width = width
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color

    def go_to(self):
        turtle.penup()
        turtle.goto(self.x_coord, self.y_coord)
        turtle.pendown()
        turtle.color(self.color)
        turtle.pensize(4)
        turtle.speed("fastest")

    def draw(self):
        turtle.forward(self.length)
        turtle.left(90)

        turtle.forward(self.width)
        turtle.left(90)
        
        turtle.forward(self.length)
        turtle.left(90)

        turtle.forward(self.width)
        turtle.left(90)

def store_rectangles():
    """
    Function -- store_rectangles()

    calling each rectangle object here to
    free up the main
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


def quit_button():
    t2 = turtle.Turtle()
    t2.penup()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif")
    t2.goto(250, -250)
    t2.pendown()
    t2.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif")

    # add the utility of this button with clicks

def load_button():
    t3 = turtle.Turtle()
    t3.penup()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif")
    t3.goto(150, -250)
    t3.pendown()
    t3.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif")

def reset_button():
    t4 = turtle.Turtle()
    t4.penup()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif")
    t4.goto(50, -250)
    t4.pendown()
    t4.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif")


    
# run this through a loop based on what puzzle is loaded
# so it will change the img with a conditional if mario or luigi...etc is chosen
def leaderboard_img():
    t5 = turtle.Turtle()
    t5.penup()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Images/luigi/luigi_thumbnail.gif")
    t5.goto(250, 220)
    t5.pendown()
    t5.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Images/luigi/luigi_thumbnail.gif")
    

# create a function to store the leaderboards
# store in a dict
# Key = name 
# Value = score
def leaderboard():
    t6 = turtle.Turtle()
    t6.penup()
    t6.goto(130, 215)
    t6.pendown()
    t6.color("blue")
    t6.write("Leaders: ", font=("Ariel", 15, "normal"))
    t6.hideturtle()
    leader = {}

    
    # need to store leaderboard in a data structure (dictionary)

def keep_score():
    """
    FUNCTION -- keep_score()

    this function keeps score and displays the 
    number of of attempts the player has performed.
    it will break if the user wins, or if the user 
    reaches their attempt limit
    """
    count = 0
    t7 = turtle.Turtle()
    t7.penup()
    t7.goto(-230, -260)
    t7.pendown()
    t7.color('blue')
    t7.write('Player Attempts: 0', font=("Ariel", 15, "normal"))
    t7.hideturtle()
    # need to iterate through count and display the total number based
    # on clicks.. 
    # cant build this fully until the click function is built.


def load_puzzle(path=GeneratePuzzle.get_mario):
    t8 = turtle.Turtle()
    t8.penup()
    t8.pendown()
    screen.addshape()
    