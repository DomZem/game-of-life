import pygame
from UI.Button import Button
from UI.CellGrid import CellGrid
from UI.ColorsConfiguration import ColorsConfiguration
from UI.Composite import Composite
from UI.Grid import Grid

# Init pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Button dimensions
button_width, button_height = 200, 50
button_x, button_y = (width - button_width) // 2, height - button_height - 10

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Colors configuration singleton
colors = ColorsConfiguration()

# Simulation control variables
running = True
tick_interval = 0.1  # in seconds
last_tick_time = pygame.time.get_ticks()

# Create UI components
button = Button(screen, button_x, button_y, button_width, button_height, colors.green,"Next Generation")
grid = Grid(screen, width, height, cell_width, cell_height)
cell_grid = CellGrid(screen, n_cells_x, n_cells_y, cell_width, cell_height)

# Create a composite for grouping components
composite = Composite()
composite.add_component(grid)
composite.add_component(cell_grid)
composite.add_component(button)


while running:
    screen.fill(colors.white)

    # Draw UI components using the composite
    composite.draw()
    pygame.display.flip()

pygame.quit()
