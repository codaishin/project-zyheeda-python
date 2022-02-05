import sys
from typing import Iterable

import pygame
from config import Settings


class Engine:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.size)
        self.clock = pygame.time.Clock()

    @staticmethod
    def start() -> None:
        pygame.init()
        pygame.display.set_caption("Game")

    def update(self) -> None:
        self.screen.fill("black")
        pygame.display.update()
        self.clock.tick(self.settings.fps)

    @staticmethod
    def quit() -> None:
        pygame.quit()
        sys.exit()

    @property
    def events(self) -> Iterable[pygame.event.Event]:
        return pygame.event.get()