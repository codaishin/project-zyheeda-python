import sys
from typing import Iterable

import pygame
from config import Settings


class Engine:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._screen = pygame.display.set_mode(settings.size)
        self._clock = pygame.time.Clock()

    @staticmethod
    def start() -> None:
        pygame.init()
        pygame.display.set_caption("Game")

    def update(self) -> None:
        self._screen.fill("black")
        pygame.display.update()
        self._clock.tick(self._settings.fps)

    @staticmethod
    def quit() -> None:
        pygame.quit()
        sys.exit()

    @staticmethod
    def pull_events() -> Iterable[pygame.event.Event]:
        return pygame.event.get()
