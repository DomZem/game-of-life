import pygame

from GameState import GameState
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

# Game state
game_state = GameState(n_cells_x, n_cells_y)

# Simulation control variables
running = True
tick_interval = 0.1  # in seconds
last_tick_time = pygame.time.get_ticks()

# Create UI components
button = Button(screen, button_x, button_y, button_width, button_height, colors.green,"Next Generation")
grid = Grid(screen, width, height, cell_width, cell_height)
cell_grid = CellGrid(screen, n_cells_x, n_cells_y, cell_width, cell_height, game_state)

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                button_x <= event.pos[0] <= button_x + button_width
                and button_y <= event.pos[1] <= button_y + button_height
            ):
                game_state.change_state()
            else:
                x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                game_state.current_state[x, y] = not game_state.current_state[x, y]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state.pause_resume()
            elif event.key == pygame.K_s:
                game_state.save()
            elif event.key == pygame.K_l:
                game_state.load()

    if not game_state.isPaused:
        current_time = pygame.time.get_ticks()
        if current_time - last_tick_time > tick_interval * 1000:
            game_state.change_state()
            last_tick_time = current_time

pygame.quit()
