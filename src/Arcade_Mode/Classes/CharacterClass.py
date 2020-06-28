from src.Common.Classes.CharacterClass import Player
from src.Common.Classes.ColorClass import Color
from src.Common.Classes.SongClasses import Song
from src.Common.Classes.PygameLoader import PygameLoader
import src.constants


pygame_loader = PygameLoader()


class ArcadePlayer(Player):
    choice_image = ""
    game_image = ""
    ignite_image = ""
    swan_song_image = ""
    choice_background_image = ""

    def __init__(self, color: Color, pos_x: int, pos_y: int, name: str, ignite_sound: Song, swan_song: Song):
        super().__init__(color, pos_x, pos_y, name)
        self.songs.add_song(ignite_sound)
        self.songs.add_song(swan_song)
        make_arcade_player(self)

    def set_choice_window_image(self):
        self.choice_image = pygame_loader.pygame_image_loader(r"{0}\src\images\concepts\{1}.png"
                                                                   .format(f"{src.constants.path_of_directory}",
                                                                           f"{self.name.lower()}_choice_window"))

    def set_choice_background_image(self):
        self.choice_background_image = pygame_loader.pygame_image_loader(r"{0}\src\images\concepts\{1}.png"
                                                                              .format(
            f"{src.constants.path_of_directory}",
            f"{self.name.lower()}_choice_background"))

    def set_game_image(self):
        self.game_image = pygame_loader.pygame_image_loader(r"{0}\src\images\characters\{1}.png"
                                                                 .format(f"{src.constants.path_of_directory}",
                                                                         f"{self.name.lower()}"))

    def set_ignite_image(self):
        self.ignite_image = pygame_loader.pygame_image_loader(r"{0}\src\images\characters\{1}.png"
                                                                   .format(f"{src.constants.path_of_directory}",
                                                                           f"{self.name.lower()}_ignite"))

    def set_swan_song_image(self):
        self.swan_song_image = pygame_loader.pygame_image_loader(r"{0}\src\images\characters\{1}.png"
                                                                      .format(f"{src.constants.path_of_directory}",
                                                                              f"{self.name.lower()}_swan"))


def make_arcade_player(player: ArcadePlayer):
    player.set_choice_window_image()
    player.set_choice_background_image()
    player.set_game_image()
    player.set_ignite_image()
    player.set_swan_song_image()
