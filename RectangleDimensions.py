import turtle
class RectangleDimensions:
    """
    Class - RectangleDimensions

    this class takes the length, width, coordinates and color
    to create a rectangle. This will be used to configure the 
    gameboard.
    """
    def __init__(self, length, width, x_coord, y_coord, color):
        self.length = length
        self.width = width
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color

    def go_to(self):
        turtle.penup()
        turtle.goto(self.x_coord, self.y_coord)
        turtle.pendown()
        turtle.color(self.color)
        turtle.pensize(4)
        turtle.speed("fastest")

    def draw(self):
        turtle.forward(self.length)
        turtle.left(90)

        turtle.forward(self.width)
        turtle.left(90)
        
        turtle.forward(self.length)
        turtle.left(90)

        turtle.forward(self.width)
        turtle.left(90)