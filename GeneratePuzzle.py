import turtle
from functions import *
import random

def get_puzzle(file_path):
    """
    METHOD -- get_fifteen

    this function stores the puzzle fifteen as a list and 
    returns the key as the index and values as the images
    """
    puzzle = []
    with open(file_path, "r") as f:
        puzzle = f.readlines()
    combine = {}
    for each in puzzle:
        puzzle = each.strip().split(": ")
        combine[puzzle[0]] = puzzle[1]
    
    # storing thumbnail in a variable
    thumbnail = combine['thumbnail']

    # storing the number of the file
    number = int(combine['number'])
    
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
    # print(keys_dict_shuffled)

    # unshuffled image path file
    img_list = []
    for i in keys_dict.keys():
        image_path = keys_dict[i]
        img_list.append(image_path)
    
    # shuffled image path files
    shuffled_img_list = []
    for i in keys_dict_shuffled.keys():
        image_path = keys_dict_shuffled[i]
        shuffled_img_list.append(image_path)
    
    # return 
    return img_list, number, shuffled_img_list
