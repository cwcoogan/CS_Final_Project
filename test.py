"""
Chase Coogan
CS 5001
Fall 2022
Final Project Testing
"""


# use this file to test classes and functionality of turtle

from turtle import *

class TestShape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        area = self.length * self.width
        return area
    
    def __str__(self):
        return "The square has an area of " + str(TestShape.get_area())

def main():
    draw = TestShape(50, 100)
    

    print(draw.get_area()) # need to make sure down here I am calling the object appropriately

if __name__ == "__main__":
    main()