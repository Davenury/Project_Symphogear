import sys
from time import sleep

sys.path.append('..')

import pygame
from src.Common.Classes.PygameLoader import PygameLoader
from src import constants
from src.Common.Classes.SongClasses import Song

song = Song("Rainbow Flower", "all_loves.ogg", False, "cokolwiek")

WIDTH = constants.width
HEIGHT = constants.height


def draw():
    background = PygameLoader.pygame_image_loader(r'{0}\src\images\instructions\\tlo.png'
                                                  .format(f"{constants.path_of_directory}"))
    screen.blit(background, (0, 0))
    song.play()
    song.fade_out(10)
    while song.is_playing():
        print(song.get_volume())
        sleep(1)
