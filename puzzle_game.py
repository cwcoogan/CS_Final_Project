"""
Chase Coogan
CS 5001
Fall 2022
puzzle_game.py
"""

from functions import *
from generate_puzzle import *
import turtle
import random

def main():
    runner = PuzzleRunner()
    runner.splash_screen()
    runner.update_leaders()
    runner.user_input()
    store_rectangles()
    runner.quit_button()
    runner.load_button()
    runner.reset_button() 
    runner.leaderboard() 
    runner.keep_score()
    runner.load_puzzle("slider_puzzle_project_fall2021_assets-2022/mario.puz")


    runner.screen.mainloop()
if __name__ == "__main__":
    main()