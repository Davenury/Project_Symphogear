import pygame


class PygameLoader:
    def __init__(self):
        pygame.mixer.init()

    @staticmethod
    def pygame_image_loader(path: str):
        return pygame.image.load(path)

    @staticmethod
    def pygame_play_music_once(path: str):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(0)

    @staticmethod
    def pygame_play_music_n_times(path: str, times: int):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(times)

    @staticmethod
    def pygame_pause_music():
        pygame.mixer.pause()

    @staticmethod
    def pygame_unpause_music():
        pygame.mixer.unpause()

    @staticmethod
    def mixer_pygame_is_playing() -> bool:
        return pygame.mixer.get_busy()

    @staticmethod
    def pygame_stop_music():
        pygame.mixer.stop()

    @staticmethod
    def pygame_music_fadeout(duration: int):
        pygame.mixer.fadeout(duration)
