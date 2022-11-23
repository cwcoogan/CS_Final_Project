"""
Chase Coogan
Fall 2022
CS 5001
helper file storing classes and functions
for the puzzle game.
"""

import turtle
import time

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
        turtle.speed(0)

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
    rectangle1 = RectangleDimensions(175, 392, 120, -150, "blue")
    rectangle1.go_to()
    rectangle1.draw()

    rectangle2 = RectangleDimensions(350, 392, -250, -150, "black")
    rectangle2.go_to()
    rectangle2.draw()

    rectangle3 = RectangleDimensions(550, 100, -250,-300, "black")
    rectangle3.go_to()
    rectangle3.draw()


def quit_button():
    t2 = turtle.Turtle()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif")
    t2.goto(250, -250)
    t2.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/quitbutton.gif")

    # add the utility of this button with clicks

def load_button():
    t3 = turtle.Turtle()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif")
    t3.goto(150, -250)
    t3.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/loadbutton.gif")

def reset_button():
    t4 = turtle.Turtle()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif")
    t4.goto(50, -250)
    t4.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Resources/resetbutton.gif")


    
# run this through a loop based on what puzzle is loaded
# so it will change the img with a conditional if mario or luigi...etc is chosen
def leaderboard_img():
    t5 = turtle.Turtle()
    screen.addshape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Images/luigi/luigi_thumbnail.gif")
    t5.goto(280, 250)
    t5.shape("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/Images/luigi/luigi_thumbnail.gif")