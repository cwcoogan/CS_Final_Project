import turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
turtle.hideturtle()
t1 = turtle.Turtle()


def get_coords(x, y):
    return get_coords


def go_to():
    x = get_coords()
    turtle.penup()
    turtle.goto(x)
    turtle.pendown()

def draw_rectangle():
    turtle.right(90)
    turtle.backward(90)
    turtle.right(90)
    turtle.backward(90)
    turtle.right(90)
    turtle.backward(80)
    turtle.right(90)
    turtle.backward(80)

class testShape:
    def __init__(self, length, width):
        self.length = length
        self.width = width


def main():
    get_coords(75, 100)
    go_to()
    draw_rectangle()

    screen.exitonclick()
if __name__ == "__main__":
    main()