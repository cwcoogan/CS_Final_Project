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

def main():
    #splash_screen()
    #user_input()
    store_rectangles()
    quit_button()
    load_button()
    reset_button() 
    leaderboard()
    keep_score()
    load_puzzle("slider_puzzle_project_fall2021_assets-2022/mario.puz")
    click_change()
    
    
    screen.mainloop()
if __name__ == "__main__":
    main()