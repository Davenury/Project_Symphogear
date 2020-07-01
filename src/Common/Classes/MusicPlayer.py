from src.Common.Classes.SongClasses import Song, SongList, make_song_list


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
