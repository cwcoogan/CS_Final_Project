import turtle
from functions import *
import random

def get_puzzle(file_path):
    """
    FUNCTION -- get_puzzle

    Parameters - file_path

    Returns - Two dictionaries - one in order, one shuffled
    Returns - Thumbnail from file and number from file 
    """

    # ---- Read File & strip/split/store as list ---- #
    puzzle = []
    with open(file_path, "r") as f:
        puzzle = f.readlines()
    combine = {}
    for each in puzzle:
        puzzle = each.strip().split(": ")
        combine[puzzle[0]] = puzzle[1]
    
                
    # ---- Storing Thumbnail as a var ---- #
    thumbnail = combine['thumbnail']

    
    # ---- Storing number as a var ---- #
    number = int(combine['number'])
    
    
    # ---- un-shuffled keys and dictionary ---- #
    keys_dict = {}
    for i in combine.keys():
        if i.isdigit():
            keys_dict[i] = combine[i]
            
    # ----  shuffled keys and dictionary ---- #
    keys = list(keys_dict.keys())
    random.shuffle(keys)
    keys_dict_shuffled = {}
    for key in keys:
        keys_dict_shuffled.update({key: keys_dict[key]})

        
    # ---- get the blank/gif img ---- #
    # get_tile = list(keys_dict_shuffled.keys())
    # get_tile.sort()
    # blank_tile = []
    # for i in get_tile:
    #     blank_tile.append(int(i))
    # blank_tile.sort()
    # blank_tile = blank_tile[-1] # prints the int value
    # blank_tile = keys_dict_shuffled[str(blank_tile)] # prints the blank img value
    # print(blank_tile) # prints the str value of y
    


    # ----  unshuffled image path file ---- #
    img_list = []
    for i in keys_dict.keys():
        image_path = keys_dict[i]
        img_list.append(image_path)
    # print(img_list) prints an ordered list of the images
        
    # ---- shuffled image path files ---- #
    shuffled_img_list = []
    for i in keys_dict_shuffled.keys():
        image_path = keys_dict_shuffled[i]
        shuffled_img_list.append(image_path)
     
    # ---- return dictionaries, number, thumbnail---- #
    return img_list, number, shuffled_img_list, thumbnail
