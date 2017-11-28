# This file contains only the cell class - behavior and properties of the individual cell

import settings

class Cell:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self.populated = False

        # make list of neighbor coords to check
        self.neighbor_coords = []
        for xdiff in range(-1,2):
            check_x = self.x + xdiff
            for ydiff in range(-1,2):
                check_y = self.y + ydiff
                # dont check cells outside grid
                if 0 <= check_x < settings.grid_width - 1 and 0 <= check_y < settings.grid_height - 1:
                    # cell shouldn't count itself
                    if not (check_x == self.x and check_y == self.y):
                        self.neighbor_coords.append((check_x,check_y))


    # counts number of neighbors
    # and decides whether to flip the tile
    def check_for_flip(self):
        # count populated neighbors
        from conway import grid
        populated_neighbors = 0
        for coord in self.neighbor_coords:
            if grid[coord[0]][coord[1]].populated:
                populated_neighbors += 1

        # then act on the result
        # for populated cells
        if self.populated:
            # cells with 0-1 neighbors die of solitude
            if populated_neighbors < 2:
                return True
            # cells with > 4 die from overpoupulation
            elif populated_neighbors > 3:
                return True
        # empty cells with three neigbors become populated
        elif populated_neighbors == 3:
            return True


    # inverts the color
    def flip(self):
        self.populated = not self.populated
