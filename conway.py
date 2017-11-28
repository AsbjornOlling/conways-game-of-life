# This file contains the main loop of the program, and all the pygame stuff.
# This is the main file to be executed

import pygame
from pygame.locals import *
import settings
from cell import Cell


def draw(cell):
    if cell.populated:
        color = settings.black
    else:
        color = settings.white
    pygame.draw.rect(gameDisplay, color, (cell.x * settings.cell_width, cell.y * settings.cell_height, settings.cell_width, settings.cell_height))


# simulation step one forward
def simulation_step():
    # iterate through grid, finding cells to flip
    cells_to_flip = []
    for x in range(0, settings.grid_width):
        for y in range(0, settings.grid_height):
            if grid[x][y].check_for_flip():
                cells_to_flip.append((x,y))

    # flip all cells at the same time
    for cell_coords in cells_to_flip:
        grid[cell_coords[0]][cell_coords[1]].flip()
        draw(grid[cell_coords[0]][cell_coords[1]])


pygame.init()

# define window
gameDisplay = pygame.display.set_mode((settings.display_width, settings.display_height)) 
pygame.display.set_caption("CONWAY")
gameDisplay.fill(settings.white)

# object that handles timing
clock = pygame.time.Clock()                      

# fill the grid with cell objects
grid = []
for x in range(0, settings.grid_width):
    column = []
    for y in range(0, settings.grid_height):
        column.append(Cell( (x,y) ))
    grid.append(column)

# spawn a strange maze builder thingamagig
grid[2][1].populated = True
grid[3][2].populated = True
grid[1][3].populated = True
grid[2][3].populated = True
grid[3][3].populated = True
draw(grid[2][1])
draw(grid[3][2])
draw(grid[1][3])
draw(grid[2][3])
draw(grid[3][3])
pygame.display.update()

# start main loop
crashed = False
paused = True
while not crashed:

    # main event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit
            crashed = True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE: # toggle pause
                paused = not paused
            elif event.key == K_RIGHT:
                simulation_step()
        elif event.type == MOUSEBUTTONUP:
            mouse_x, mouse_y = event.pos
            cell_x = int(mouse_x / settings.cell_width)
            cell_y = int(mouse_y / settings.cell_height)
            grid[cell_x][cell_y].flip()
            draw(grid[cell_x][cell_y])
    
    if not paused:
        simulation_step()

    # update entire screen
    pygame.display.update()

    # wait 1/60 second
    clock.tick(60)

pygame.quit()
quit()
