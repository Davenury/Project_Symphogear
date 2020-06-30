import pygame
from src.Common.Classes.ColorClass import Color


class TextDisplayer:
    def __init__(self, font_name: str = 'comicsansms', font_size: int = 15):
        pygame.font.init()
        self.font = pygame.font.SysFont(font_name, font_size)
        self.font_size = font_size

    def make_text_surface(self, color: Color, text: str):
        return self.font.render(text, False, (color.red, color.green, color.blue))
