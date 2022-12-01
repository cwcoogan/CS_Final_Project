import turtle

class Tile:
    def __init__(self, x, y, img_file, screen, location=(0, 0), count=-1) -> None:
        self.t = turtle.Turtle()
        self.t.speed("fastest")
        self.x = x
        self.y = y
        self.location = location
        self.img_file = img_file
        self.screen = screen
        self.puzzle = ""
        self.count = count

        self.blank = False

        if img_file:            
            if img_file[-9:-4] == "blank":
                self.blank = True
            turtle.register_shape(img_file)

    def display_img(self):
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.shape(self.img_file)
    
    def goto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def set_puzzle(self, puz):
        self.puzzle = puz
        
    def get_puzzle(self, puz):
        return self.puzzle

    def display_text(self, text, txt_size):
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.write(text, font=("Ariel", txt_size, "normal"))