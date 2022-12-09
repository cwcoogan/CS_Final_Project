
class Puzzle:
    def __init__(self, path) -> None:
        """
        Method -- __init__

        Parameter -- self, path

        Returns -- path of files and an empty list
        """
        self.path = path
        self.tiles = []

    def get_path(self):
        """
        Method -- get_path

        Parameter -- self

        Returns -- getter method to get paths
        """
        return self.path
    
    def get_tiles(self):
        """
        Method -- get_tiles

        Parameter -- self

        Returns -- self.tiles
        """
        return self.tiles
    
    def get_thumbnail(self):
        """
        Method -- get_thumbnail

        Parameter - self

        Returns -- getter to retreive thumbnails
        """
        return self.thumbnail

    def set_thumbnail(self, t):
        """
        Method -- set_thumbnail

        Parameter -- self, t

        Returns -- setter for thumbnails
        """
        self.thumbnail = t
    
    def clear(self):
        """
        Method -- clear

        Parameter -- self

        Returns -- helper function to help clear
                   the tiles and then re-display then
                   calls the get_thumbnail method
        """
        for row in self.tiles:
            for tile in row:
                tile.t.hideturtle()
    
        self.get_thumbnail().t.hideturtle()
    
    def swap_tiles(self, a, b):
        """
        Method -- swap_tiles

        Parameter -- self, a, b

        Returns -- logic stored here to get the ax, ay, bx, by 
                   coordinates that will be used to swap based on
                   their location in the screen. 
        """
        ax, ay = a.x, a.y
        bx, by = b.x, b.y

        a.x, b.x = b.x, a.x
        a.y, b.y = b.y, a.y

        a.goto(bx, by)
        b.goto(ax, ay)

        ai, aj = a.location
        bi, bj = b.location

        a.location, b.location = b.location, a.location

        self.tiles[ai][aj], self.tiles[bi][bj] = self.tiles[bi][bj], self.tiles[ai][aj]
        