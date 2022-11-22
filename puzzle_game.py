"""
Chase Coogan
CS 5001
Fall 2022
puzzle_game.py
"""

from functions import *
import turtle


# initialize turtle
screen = turtle.Screen()

def main():
    splash_screen()
    user_input()
    store_rectangles()

    screen.exitonclick()
if __name__ == "__main__":
    main()