import pygame

from src.Common.Classes.Exceptions import WrongKeyException, ChangedSongException
from src.Common.Classes.SongClasses import Song, SongList, make_song_list, NoSongException


class MusicPlayer:
    def __init__(self, songs):
        self.song_list = make_song_list(songs)
        self.paused = False

    def play_song_once(self):
        self.song_list.play_this_song()
        return self.song_list.list[self.song_list.index]

    def play_song_infinitely(self):
        self.song_list.play_this_song_n_times(-1)
        return self.song_list.list[self.song_list.index]

    def play_next_song(self):
        song = self.song_list.get_next_song()
        song.play()
        return self.song_list.list[self.song_list.index]

    def play_previous_song(self):
        song = self.song_list.get_previous_song()
        song.play()
        return self.song_list.list[self.song_list.index]

    def change_paused_status(self):
        if self.paused:
            self.song_list.list[self.song_list.index].unpause()
            self.paused = False
        else:
            self.song_list.list[self.song_list.index].pause()
            self.paused = True

    def play(self):
        return self.play_song_infinitely()

    def stop(self):
        self.song_list.list[self.song_list.index].stop()

    def parse_events(self, event, song: Song):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                song = self.play_next_song()
                raise ChangedSongException(song)
            elif event.key == pygame.K_LEFT:
                song = self.play_previous_song()
                raise ChangedSongException(song)
            elif event.key == pygame.K_SPACE:
                self.change_paused_status()
                return song
            elif event.key == pygame.K_p:
                song = self.play()
                return song
            elif event.key == pygame.K_e:
                self.stop()
                raise NoSongException()
            else:
                raise WrongKeyException()
        else:
            return song

    def start(self, make_screen):
        song = self.play_song_infinitely()
        make_screen(song)
        while True:
            for event in pygame.event.get():
                try:
                    song = self.parse_events(event, song)
                except WrongKeyException:
                    print("User pressed wrong key!")
                except ChangedSongException as e:
                    self.play_song_infinitely()
                    make_screen(e.get_song())
                except NoSongException:
                    song = Song("No song chosen", "None", False, "no_song_cover")
