import matplotlib.pyplot as plt
from GameOfLife.Grid import Grid

class GameOfLife:
    def play(self, rows, cols):
        grid = Grid(rows, cols)
        grid.come_alive()
        fg = plt.figure()
        ax = fg.gca()
        board = ax.imshow(grid.self())
        some_alive = True
        while (some_alive):
            grid, some_alive = self.next_grid_state(grid)
            board.set_data(grid.self())
            plt.draw()
            plt.pause(1e-3)

    def next_grid_state(self, grid):
        next_grid = Grid(grid.rows, grid.cols)
        some_alive = False 
        for i in range(grid.rows):
            for j in range (grid.cols):
                next_grid.set((i,j), self.next_cell_state(grid, i, j))
                if next_grid.get((i,j)) == 1: some_alive = True
        return next_grid, some_alive

    def next_cell_state(self, grid, x, y):
        cell = grid.get((x, y))
        num_alive_neighbors = self.find_alive_neighbors(grid, cell, x, y)
        if (cell == 1):
            if (self.overpopulation(num_alive_neighbors) or self.underpopulation(num_alive_neighbors)): 
                return 0
        elif (self.reproduction(num_alive_neighbors)): 
            return 1
        return cell

    def overpopulation(self, num_alive_neighbors):
        return num_alive_neighbors > 3
    
    def underpopulation(self, num_alive_neighbors):
        return num_alive_neighbors < 2

    def reproduction(self, num_alive_neighbors):
        return num_alive_neighbors == 3

    def find_alive_neighbors(self, grid, cell_value, x, y):
        xmin = 0
        ymin = 0
        xmax = grid.rows - 1
        ymax = grid.cols - 1
        count = 0
        if (x > xmin):
            if (y > ymin and grid.get((x - 1, y - 1)) == 1): count += 1
            if (y < ymax and grid.get((x - 1, y + 1))): count += 1
            if (grid.get((x - 1,y)) == 1): count += 1
        if (x < xmax):
            if (y > ymin and grid.get((x + 1, y - 1)) == 1): count += 1
            if (y < ymax and grid.get((x + 1, y + 1))): count += 1
            if (grid.get((x +1, y)) == 1): count += 1
        if (y > ymin and grid.get((x, y - 1)) == 1): count += 1
        if (y < ymax and grid.get((x, y + 1))): count += 1
        return count

