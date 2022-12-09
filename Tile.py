import turtle

class Tile:
    def __init__(self, x, y, img_file, screen, location=(0, 0), count=-1) -> None:
        """
        Method -- __init__

        Parameters -- self, x, y, img_file, screen, location, count

        Returns -- turtle object, (x,y) coordinates, img_file path, 
                   screen, location on screen, a counter
        """
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
        """
        Method -- display_img

        Parameters -- self

        Returns -- goes to img_file path (x,y coords) and
                   displays the image
        """
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.shape(self.img_file)
    
    def goto(self, x, y):
        """
        Method -- goto

        Parameters -- self, x, y

        Returns --  turtle goes to (x,y) coords and pens down
        """
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def set_puzzle(self, puz):
        """
        Method -- set_puzzle

        Parameter -- self, puz

        Returns --  setter for puzzle
        """
        self.puzzle = puz
        
    def get_puzzle(self, puz):
        """
        Method -- get_puzzle

        Parameter -- self, puz

        Returns -- getter for puzzle
        """
        return self.puzzle

    def display_text(self, text, txt_size):
        """
        Method -- display_text

        Parameter -- self, text, txt_size

        Returns -- Turtle goes to (x,y) coordinate, places
                   pen down & writes the text and sets font size
        """
        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()
        self.t.write(text, font=("Ariel", txt_size, "normal"))