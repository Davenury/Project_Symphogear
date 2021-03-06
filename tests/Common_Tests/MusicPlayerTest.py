import sys
import pygame

sys.path.append('../..')

from src.Common.Classes.SongClasses import Song
from src.Common.Classes.Exceptions import WrongKeyException, ChangedSongException
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

song = ""


def make_screen(cover):
    screen.blit(cover, (0, 0))
    pygame.display.flip()


def parse_events(event):
    global song
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            song = music_player.play_next_song()
            raise ChangedSongException()
        elif event.key == pygame.K_LEFT:
            song = music_player.play_previous_song()
            raise ChangedSongException()
        else:
            raise WrongKeyException()
    else:
        return song


def draw():
    global song
    song = music_player.play_song_infinitely()

    while True:
        make_screen(song.get_cover())
        for event in pygame.event.get():
            try:
                song = parse_events(event)
            except WrongKeyException:
                print("User pressed wrong key!")
            except ChangedSongException:
                music_player.play_song_infinitely()
