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
    keep_score()
    load_puzzle("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/mario.puz")
    

    screen.mainloop()
if __name__ == "__main__":
    main()