import sys
import pygame

sys.path.append('../..')

from src.Common.Classes.SongClasses import Song
from src.Common.Classes.Exceptions import WrongKeyException
from src.Common.Classes.MusicPlayer import MusicPlayer
from src.Common.Classes.PygameLoader import PygameLoader
from src import constants
from time import sleep

WIDTH = constants.cover_width
HEIGHT = constants.cover_height

# music_player = MusicPlayer(constants.hibiki_songs)  WORKS
# music_player = MusicPlayer(constants.tsubasa_songs) WORKS
# music_player = MusicPlayer(constants.chris_songs)    WORKS
# music_player = MusicPlayer(constants.maria_songs)   WORKS
# music_player = MusicPlayer(constants.shirabe_songs) WORKS
# music_player = MusicPlayer(constants.kirika_songs) WORKS
# music_player = MusicPlayer(constants.miku_songs) WORKS
music_player = MusicPlayer(constants.all_songs)  # I think it works too


def make_screen(cover):
    screen.blit(cover, (0, 0))
    pygame.display.flip()


def parse_events(event, current_song: Song):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            current_song = music_player.play_next_song()
        elif event.key == pygame.K_LEFT:
            current_song = music_player.play_previous_song()
        elif event.key == pygame.K_i:
            current_song = music_player.play_song_infinitely()
        else:
            raise WrongKeyException()
        return current_song
    else:
        return current_song


def draw():
    song = music_player.play_song_infinitely()

    while True:
        make_screen(song.get_cover())
        for event in pygame.event.get():
            try:
                song = parse_events(event, song)
            except WrongKeyException:
                print("User pressed wrong key!")
