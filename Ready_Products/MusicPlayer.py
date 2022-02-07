import sys
sys.path.append("..")

from src import constants
from src.Common.Classes.ColorClass import Color
from src.Common.Classes.Exceptions import WrongKeyException, ChangedSongException
from src.Common.Classes.MusicPlayer import MusicPlayer
import pygame

from src.Common.Classes.SongClasses import Song, NoSongException
from src.Common.Classes.TextDisplayer import TextDisplayer

WIDTH = constants.cover_width
HEIGHT = constants.cover_height + constants.place_for_text_height

music_player = MusicPlayer(constants.all_songs)
text_displayer = TextDisplayer()


def make_screen(current_song: Song):
    screen.fill((0, 0, 0))
    screen.blit(current_song.get_cover(), (0, constants.place_for_text_height))
    text = text_displayer.make_text_surface(Color(0, 128, 255),
                                            current_song.get_title())
    text_rect = text.get_rect(center=(WIDTH / 2, (constants.place_for_text_height -
                                                  text_displayer.font_size) / 2 + 10))
    screen.blit(text, text_rect)
    pygame.display.flip()


def draw():
    music_player.start(make_screen)

