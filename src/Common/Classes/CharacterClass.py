from .ColorClass import Color
from .SongClasses import Song, SongList


class Character:
    def __init__(self, pos_x: int, pos_y: int, name: str):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name

    def speak(self, text: str):
        print(text)     # domyślnie mówienie na ekranie Pygame

    def get_name(self) -> str:
        return self.name


class Player(Character):
    def __init__(self, color: Color, pos_x: int, pos_y: int, name: str):
        super().__init__(pos_x, pos_y, name)
        self.color = color
        self.songs = SongList()
        self.sounds = SongList()

    def move_to(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_by(self, pos_x, pos_y):
        self.pos_x += pos_x
        self.pos_y += pos_y

    def add_song(self, song: Song):
        self.songs.add_song(song)

    def add_songs_list(self, songs: SongList):
        self.songs += songs


class NPC(Character):
    pass
