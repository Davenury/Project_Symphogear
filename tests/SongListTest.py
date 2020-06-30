import unittest
from src.Common.Classes.SongClasses import Song, SongList, NoSongException


class SongListTest(unittest.TestCase):

    def next_song_test(self):
        # given
        song = Song("title1", "file1", False, "none")
        song2 = Song("title2", "file2", False, "none")
        song_list = SongList()
        song_list.add_song(song)
        song_list.add_song(song2)

        # when then
        self.assertEqual(song_list.get_next_song().get_title(), "title2")
        self.assertEqual(song_list.get_next_song().get_title(), "title1")

    def previous_song_test(self):
        # given
        song = Song("title1", "file1", False, "none")
        song2 = Song("title2", "file2", False, "none")
        song3 = Song("title3", "file3", False, "none")
        song_list = SongList()
        song_list.add_song(song)
        song_list.add_song(song2)
        song_list.add_song(song3)

        # when then
        self.assertEqual(song_list.get_previous_song().get_title(), "title3")
        self.assertEqual(song_list.get_previous_song().get_title(), "title2")

    def empty_list_next_previous_test(self):
        #given
        song_list = SongList()

        #when then
        with self.assertRaises(NoSongException) as cm:
            song_list.get_next_song()
        self.assertEqual(
            'No song in list',
            str(cm.exception)
        )
        with self.assertRaises(NoSongException) as cm:
            song_list.get_previous_song()
        self.assertEqual(
            'No song in list',
            str(cm.exception)
        )

    def get_title_test(self):
        # given
        song = Song("title1", "file1", False, "none")
        song2 = Song("title2", "file2", False, "none")
        song_list = SongList()
        song_list.add_song(song)
        song_list.add_song(song2)

        # when
        try:
            tried_song = song_list.get_song_by_title("title1")
        except NoSongException:
            self.fail("Unexpected Exception!")

        # then
        self.assertEquals("title1", tried_song.get_title())

    def remove_song_from_list_test(self):
        # given
        song = Song("title1", "file1", False, "none")
        song2 = Song("title2", "file2", True, "none")
        song_list = SongList()
        song_list.add_song(song)
        song_list.add_song(song2)

        # when
        song_list.delete_song("title1")
        song_list.delete_song("title2")

        # then
        self.assertEquals(song_list.quantity, 0)


if __name__ == "__main__":
    unittest.main()
