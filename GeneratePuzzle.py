import turtle
from functions import *
import random


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
    

    def get_mario():
        """
        METHOD -- get_fifteen

        this function stores the puzzle fifteen as a list and 
        returns the key as the index and values as the images
        """
        puzzle = []
        with open("/Users/chasecoogan/Documents/CS_Final_Project/slider_puzzle_project_fall2021_assets-2022/mario.puz", "r") as f:
            puzzle = f.readlines()
        combine = {}
        for each in puzzle:
            puzzle = each.strip().split(": ")
            combine[puzzle[0]] = puzzle[1]
        # print(combine)

        # storing thumbnail in a variable
        thumbnail = combine['thumbnail']

        # un-shuffled keys and dictionary
        keys_dict = {}
        for i in combine.keys():
            if i.isdigit():
                keys_dict[i] = combine[i]
        # print(keys_dict)


        # shuffled keys and dictionary
        keys = list(keys_dict.keys())
        random.shuffle(keys)

        keys_dict_shuffled = {}
        for key in keys:
            keys_dict_shuffled.update({key: keys_dict[key]})
        print(keys_dict_shuffled)

        # unshuffled image path file
        img_list = []
        for i in keys_dict.keys():
            image_path = keys_dict[i]
            img_list.append(image_path)
        
        return img_list

        # shuffled image path files
        for i in keys_dict_shuffled.keys():
            image_path = keys_dict_shuffled[i]
        

