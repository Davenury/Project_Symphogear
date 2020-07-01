import pygame

from src.Common.Classes.PygameLoader import PygameLoader
from src.constants import path_of_directory


class NoSongException(Exception):
    """Raised when there is no such song in the list"""
    pass


class Song:
    def __init__(self, title: str, file: str, in_use: bool, cover_file: str):
        self.title = title
        self.file = path_of_directory + '\src\music\\' + file
        self.in_use = in_use
        self.cover_file = cover_file

    def play(self):
        PygameLoader.pygame_play_music_once(self.file)

    #plays song n times, where -1 means infinitely
    def play_n_times(self, n: int):
        PygameLoader.pygame_play_music_n_times(self.file, n)

    @staticmethod
    def pause():
        PygameLoader.pygame_pause_music()

    @staticmethod
    def unpause():
        PygameLoader.pygame_unpause_music()

    @staticmethod
    def stop():
        PygameLoader.pygame_stop_music()

    @staticmethod
    def fade_out(duration: int = 2):  # duration is in miliseconds
        PygameLoader.pygame_music_fadeout(duration * 1000)

    @staticmethod
    def is_playing():
        return PygameLoader.mixer_pygame_is_playing()

    def get_title(self) -> str:
        return self.title

    def get_file(self) -> str:
        return self.file

    def is_in_use(self) -> bool:
        return self.in_use

    def get_cover(self):
        return PygameLoader.pygame_image_loader(r"{0}\src\images\albums\{1}.png"
                                                .format(f"{path_of_directory}",
                                                        f"{self.cover_file}"))


class SongList:
    def __init__(self):
        self.list = []
        self.index = 0
        self.quantity = 0

    def add_song(self, song: Song):
        self.list.append(song)
        self.quantity += 1

    def delete_song(self, title: str):
        song = Song(title, "", False, "none")
        try:
            self.list.remove(song)
            self.quantity -= 1
        except ValueError:
            print(f"Song ${title} wasn't in the list")

    def get_song_by_title(self, title: str) -> Song:
        for song in self.list:
            if song.get_title() == title:
                return song
        raise NoSongException("There was no song with this title")

    def get_next_song(self) -> Song:
        if self.quantity == 0:
            raise NoSongException("No song in list")
        self.index = (self.index + 1) % self.quantity
        return self.list[self.index]

    def get_previous_song(self) -> Song:
        if self.quantity == 0:
            raise NoSongException("No song in list")
        self.index = (self.index - 1) % self.quantity
        return self.list[self.index]

    def play_this_song(self):
        if self.quantity == 0:
            raise NoSongException("No song in list")
        self.list[self.index].play()

    def play_this_song_n_times(self, n: int):
        if self.quantity == 0:
            raise NoSongException("No song in list")
        self.list[self.index].play_n_times(n)


def make_song_list(songs):
    song_list = SongList()
    for song in songs:
        song = make_song(song[0], song[1], song[2], song[3])
        song_list.add_song(song)
    return song_list


def make_song(title: str, file: str, in_use: bool, cover_file: str):
    return Song(title, file, in_use, cover_file)
