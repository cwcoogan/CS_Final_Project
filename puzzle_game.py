"""
Chase Coogan
CS 5001
Fall 2022
puzzle_game.py
"""

from functions import *
from GeneratePuzzle import *
import turtle
import random

# initialize turtle
screen = turtle.Screen()

def main():
    #splash_screen()
    #user_input()
    store_rectangles()
    quit_button()
    load_button()
    reset_button()
    leaderboard_img()
    leaderboard()
    GeneratePuzzle.get_mario()
    keep_score()
    load_puzzle()
    
    

    screen.exitonclick()
if __name__ == "__main__":
    main()