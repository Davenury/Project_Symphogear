import pygame


class PygameLoader:

    @staticmethod
    def pygame_image_loader(path: str):
        return pygame.image.load(path)

    @staticmethod
    def pygame_make_sound(path: str):
        if pygame.mixer.get_init is None:
            pygame.mixer.init()
        return pygame.mixer.Sound(path)

    @staticmethod
    def pygame_pause_music():
        pygame.mixer.pause()

    @staticmethod
    def pygame_unpause_music():
        pygame.mixer.unpause()

    @staticmethod
    def mixer_pygame_is_playing() -> bool:
        return pygame.mixer.get_busy()