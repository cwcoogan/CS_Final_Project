from turtle import *
from RectangleDimensions import *

"""
THIS FILE STORES THE RECTANGLE FUNCTION
CLEANING UP MY CODE*****
"""



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

