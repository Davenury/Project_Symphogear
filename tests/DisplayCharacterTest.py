import pygame
import sys
sys.path.append('..')

from src.Common.Classes import SongClasses
from src.Common.Classes import ColorClass
from src.Arcade_Mode.Classes import CharacterClass
import src.constants
from src.Common.Classes.PygameLoader import PygameLoader
from src import images

WIDTH = src.constants.width
HEIGHT = src.constants.height
pygame.init()

character = CharacterClass.ArcadePlayer(ColorClass.Color(255, 255, 255),
                                        0, 0, "Hibiki", SongClasses.Song("title", "file", False, "cover"),
                                        SongClasses.Song("title", "file", False, "cover"))


def draw():
    background = PygameLoader.pygame_image_loader(r'{0}\src\images\instructions\\tlo.png'
                                                  .format(f"{src.constants.path_of_directory}"))
    screen.blit(background, (0, 0))
    screen.blit(character.ignite_image, (0, 0))
