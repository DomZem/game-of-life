import pygame

from UI.Component import Component


class CellGrid(Component):
    def __init__(self, screen, n_cells_x, n_cells_y, cell_width, cell_height, game_state, alive_color=(0, 0, 0)):
        self.screen = screen
        self.n_cells_x = n_cells_x
        self.n_cells_y = n_cells_y
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.game_state = game_state
        self.alive_color = alive_color

    def draw(self):
        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                cell = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                if self.game_state.current_state[x, y] == 1:
                    pygame.draw.rect(self.screen, self.alive_color, cell)

