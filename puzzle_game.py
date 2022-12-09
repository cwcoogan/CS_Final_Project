"""
Chase Coogan
CS 5001
Fall 2022
puzzle_game.py
"""

from functions import *
from generate_puzzle import *


def main():
    runner = PuzzleRunner()
    runner.begin_game()
    runner.load_puzzle("slider_puzzle_project_fall2021_assets-2022/mario.puz")


    runner.screen.mainloop()
if __name__ == "__main__":
    main()