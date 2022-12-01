import math
from Tile import Tile
from pprint import pprint

class Puzzle:
    def __init__(self, path) -> None:
        self.path = path
        self.tiles = []

    def get_path(self):
        return self.path
    
    def get_tiles(self):
        return self.tiles
    
    def get_thumbnail(self):
        return self.thumbnail

    def set_thumbnail(self, t):
        self.thumbnail = t
    
    def clear(self):
        for row in self.tiles:
            for tile in row:
                tile.t.hideturtle()
    
        self.get_thumbnail().t.hideturtle()
    
    def swap_tiles(self, a, b):
        ax, ay = a.x, a.y
        bx, by = b.x, b.y

        a.x, b.x = b.x, a.x
        a.y, b.y = b.y, a.y

        a.goto(bx, by)
        b.goto(ax, ay)

        ai, aj = a.location
        bi, bj = b.location

        a.location, b.location = b.location, a.location

        data_a = self.tiles[ai][aj]
        data_b = self.tiles[bi][bj]

        data_a, data_b = data_b, data_a