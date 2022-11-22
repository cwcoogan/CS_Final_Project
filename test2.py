import turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
turtle.hideturtle()



class RectangleDimensions:
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
        turtle.speed(0)
    

    def draw(self):
        turtle.forward(self.length)
        turtle.left(90)

        turtle.forward(self.width)
        turtle.left(90)
        
        turtle.forward(self.length)
        turtle.left(90)

        turtle.forward(self.width)
        turtle.left(90)


def main():
    test = RectangleDimensions(300, 90, 50, 0, "blue")
    test.go_to()
    test.draw()
    screen.exitonclick()
if __name__ == "__main__":
    main()