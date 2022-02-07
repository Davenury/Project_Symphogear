from src.Common.Classes.SongClasses import Song


class WrongKeyException(Exception):
    """Raised when User press wrong key"""
    pass


class ChangedSongException(Exception):
    """Not so much exception, just raised when user changes the song"""
    def __init__(self, song: Song):
        self.song = song

    def get_song(self):
        return self.song
