"""
Chase Coogan
CS 5001
Fall 2022
Final Project Testing
"""

import turtle
import time

# initialize turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
turtle.hideturtle()
# screen.update()


def splash_screen():
    """
    Function splash_screen

    initializes the splash screen and sets it to appear 
    for 3 total seconds and then it goes away
    """
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
    def __init__(self, length, width, x_coord, y_coord):
        self.length = length
        self.width = width
        self.x = x_coord
        self.y = y_coord

    def go_to(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

    def draw(self):
        turtle.right(self.length)
        turtle.backward(self.width)
        turtle.right(self.length)
        turtle.backward(self.width)

def main():
    splash_screen()
    user_input()

    # screen.exitonclick()
if __name__ == "__main__":
    main()