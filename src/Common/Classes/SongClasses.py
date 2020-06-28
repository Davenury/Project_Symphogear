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
        self.sound = PygameLoader.pygame_make_sound(self.file)

    def play(self):
        self.sound.play()

    @staticmethod
    def pause():
        PygameLoader.pygame_pause_music()

    @staticmethod
    def un_pause():
        PygameLoader.pygame_unpause_music()

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume: float):
        self.sound.set_volume(volume)

    def get_volume(self):
        return self.sound.get_volume()

    def fade_out(self, duration: int = 2):  # duration is in miliseconds
        self.sound.fadeout(duration*1000)

    @staticmethod
    def is_playing():
        return PygameLoader.mixer_pygame_is_playing()

    def get_title(self) -> str:
        return self.title

    def get_file(self) -> str:
        return self.file

    def is_in_use(self) -> bool:
        return self.in_use

    def get_cover_file(self) -> str:
        return self.cover_file


class SongList:
    def __init__(self):
        self.list = []
        self.index = 0
        self.quantity = 0

    def add_song(self, song: Song):
        self.list.append(song)
        self.quantity += 1

    def delete_song(self, title: str):
        song = Song(title, "", False)
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


def make_song_list(songs):
    song_list = SongList()
    for song in songs:
        song_list.add_song(song)
    return song_list


def make_song(title: str, file: str, in_use: bool):
    return Song(title, file, in_use)
