import pygame

from UI.Component import Component


class Button(Component):
    def __init__(self, screen, x, y, width, height, button_color, text, font_size=36, text_color=(0, 0, 0)):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.button_color = button_color

    def draw(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))
        self.screen.blit(text_surface, text_rect)