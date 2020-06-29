from src.Common.Classes.CharacterClass import Player
from src.Common.Classes.ColorClass import Color
from src.Common.Classes.SongClasses import Song
from src.Common.Classes.PygameLoader import PygameLoader
from src.Common.Classes.CharacterClass import Character
from src import constants
from src.Common.Classes.BonusClass import Bonus

pygame_loader = PygameLoader()


class Attacker:
    def __init__(self):
        self.attack = constants.attack
        self.HP = constants.HP
        self.defense_bonus = Bonus()
        self.attack_bonus = Bonus()

    def attack(self, opponent):
        # 1 - defense_bonus, because if you have 30% of defense_bonus, you still
        # get 70% of damage
        opponent.HP = opponent.HP - (self.get_attack() * (1 - opponent.get_defence_bonus()))

    def get_attack(self) -> float:
        return self.attack * (1 + self.get_attack_bonus())

    def set_defense_bonus(self, defense_bonus: float):
        self.defense_bonus.set_value(defense_bonus)

    def get_defence_bonus(self) -> float:
        return self.defense_bonus.value

    def set_attack_bonus(self, attack_bonus: float):
        self.attack_bonus.set_value(attack_bonus)

    def get_attack_bonus(self) -> float:
        return self.attack_bonus.value


class ArcadePlayer(Player, Attacker):
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
                                                              .format(f"{constants.path_of_directory}",
                                                                      f"{self.name.lower()}_choice_window"))

    def set_choice_background_image(self):
        self.choice_background_image = pygame_loader.pygame_image_loader(r"{0}\src\images\concepts\{1}.png"
            .format(
            f"{constants.path_of_directory}",
            f"{self.name.lower()}_choice_background"))

    def set_game_image(self):
        self.game_image = pygame_loader.pygame_image_loader(r"{0}\src\images\characters\{1}.png"
                                                            .format(f"{constants.path_of_directory}",
                                                                    f"{self.name.lower()}"))

    def set_ignite_image(self):
        self.ignite_image = pygame_loader.pygame_image_loader(r"{0}\src\images\characters\{1}.png"
                                                              .format(f"{constants.path_of_directory}",
                                                                      f"{self.name.lower()}_ignite"))

    def set_swan_song_image(self):
        self.swan_song_image = pygame_loader.pygame_image_loader(r"{0}\src\images\characters\{1}.png"
                                                                 .format(f"{constants.path_of_directory}",
                                                                         f"{self.name.lower()}_swan"))


class ArcadeOpponent(Character, Attacker):
    pass


def make_arcade_player(player: ArcadePlayer):
    player.set_choice_window_image()
    player.set_choice_background_image()
    player.set_game_image()
    player.set_ignite_image()
    player.set_swan_song_image()
