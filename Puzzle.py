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