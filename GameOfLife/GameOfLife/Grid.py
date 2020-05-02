import numpy as np

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros(shape=(rows, cols), dtype=int)

    def set(self, position, value):
        x, y = position
        self.grid[x][y] = value

    def get(self, position):
        x, y = position
        return self.grid[x][y]
   
    def self(self):
        return self.grid

    def come_alive(self):
        self.grid = np.random.randint(2, size=(self.rows, self.cols), dtype=int)


