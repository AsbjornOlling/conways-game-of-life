import pygame


pygame.init()

# set resolution
display_width = 800
display_height = 600

# define grid
grid_width = 80  # dimensions in cells
grid_height = 60
cell_width = display_width / grid_width  # cell dimensions in pixels
cell_height = display_height / grid_height
grid = []

# colors
black = (0,0,0)
white = (255,255,255)

# define window
gameDisplay = pygame.display.set_mode((display_width, display_height)) 
pygame.display.set_caption("CONWAY")
gameDisplay.fill(white)

# behavior for the cells
# this is the core off the game
class Cell:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self.populated = False

    # 
    def check_for_flip(self):
        # count populated neighbors
        populated_neighbors = 0
        for xdiff in range(-1,2):
            check_x = self.x + xdiff
            for ydiff in range(-1,2):
                check_y = self.y + ydiff
                # dont check cells outside grid
                if 0 <= check_x < grid_width - 1 and 0 <= check_y < grid_height - 1:
                    # cell shouldn't count itself
                    if not grid[check_x][check_y] == self:
                        if grid[check_x][check_y].populated:
                            populated_neighbors += 1
        # then act on the result
        # for populated cells
        if self.populated:
            # cells with 0-1 neighbors die of solitude
            if populated_neighbors < 2:
                return True
            # cells with > 4 die from overpoupulation
            elif populated_neighbors > 4:
                return True
        # empty cells with three neighbors become populated
        elif populated_neighbors == 3:
            return True


    def flip(self):
        if self.populated:
            self.populated = False
        else:
            self.populated = True


    def draw(self):
        if self.populated:
            color = black
        else:
            color = white
        pygame.draw.rect(gameDisplay, color, (self.x * cell_width, self.y * cell_height, cell_width, cell_height))

## end class


# fill the grid with cell objects
for x in range(0, grid_width):
    column = []
    for y in range(0, grid_height):
        column.append(Cell( (x,y) ))
    grid.append(column)

# spawn a strange maze builder thingamagig
grid[2][1].populated = True
grid[3][2].populated = True
grid[1][3].populated = True
grid[2][3].populated = True
grid[3][3].populated = True

grid[2][1].draw()
grid[3][2].draw()
grid[1][3].draw()
grid[2][3].draw()
grid[3][3].draw()

# object that handles timing
clock = pygame.time.Clock()                      

pygame.display.update()

# start main loop
crashed = False
while not crashed:

    # main event handler
    for event in pygame.event.get():

        # exit event
        if event.type == pygame.QUIT:
            crashed = True

    # iterate through grid, finding cells to flip
    cells_to_flip = []
    for x in range(0, grid_width):
        for y in range(0,grid_height):
            if grid[x][y].check_for_flip():
                cells_to_flip.append((x,y))

    # flip all cells at the same time
    for cell_coords in cells_to_flip:
        grid[ cell_coords[0] ][ cell_coords[1] ].flip()
        grid[ cell_coords[0] ][ cell_coords[1] ].draw()

    # update entire screen
    pygame.display.update()

    # wait 1/60 second
    clock.tick(60)

pygame.quit()
quit()
