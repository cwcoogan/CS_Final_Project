import turtle

class Tile:
    def __init__(self, x, y, img_file, screen) -> None:
        self.t = turtle.Turtle()
        self.t.speed("fastest")
        self.x = x
        self.y = y
        self.img_file = img_file
        self.screen = screen
        self.puzzle = ""
        turtle.register_shape(img_file)

    def display_img(self):
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.shape(self.img_file)

    def set_puzzle(self, puz):
        self.puzzle = puz
        
    def get_puzzle(self, puz):
        return self.puzzle
