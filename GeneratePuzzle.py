import turtle
from functions import *

"""
NOT DONE *** Need to traverse every puzzle and store each imgs # of imgs as 
the key and the .gif as the value
"""


class GeneratePuzzle:
    """
    class GeneratePuzzle

    this class will store all the puzzle images and retrieve them individually

    and load them into a data structure
    """
    def __init__(self, fifteen, luigi, malformed, mario, smiley, yoshi):
        self.fifteen = fifteen
        self.luigi = luigi
        self.malformed = malformed
        self.mario = mario
        self.smiley = smiley
        self.yoshi = yoshi
    
    def store_puzzle():
        """
        FUNCTION -- store_puzzle()

        this function will store the images as a list
        to make scrambling easier

        data structure used is a list
        """
        puzzle = []
        return puzzle    
    
    def get_fifteen():
        puzzle = []
        with open("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/fifteen.puz", "r") as f:
            puzzle = f.readlines()
        for each in puzzle:
            puzzle = each.split()
            print(puzzle)

    def get_luigi():
        pass

    def get_malformed():
        pass

    def get_mario():
        pass

    def get_smiley():
        pass

    def get_yoshi():
        pass
    