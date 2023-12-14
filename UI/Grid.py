import pygame

from UI.Component import Component


class Grid(Component):
    def __init__(self, screen, width, height, cell_width, cell_height, line_color=(128, 128, 128)):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.line_color = line_color

    def draw(self):
        for y in range(0, self.height, self.cell_height):
            for x in range(0, self.width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, self.line_color, cell, 1)