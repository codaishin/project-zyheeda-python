from typing import Iterable, Protocol

from pygame import QUIT
from pygame.event import Event


class EngineProtocol(Protocol):
    def start(self) -> None:
        ...

    def update(self) -> None:
        ...

    def quit(self) -> None:
        ...

    @property
    def events(self) -> Iterable[Event]:
        ...


# pylint: disable=too-few-public-methods
class Game:
    """The game"""

    def __init__(self, engine: EngineProtocol) -> None:
        self.engine = engine
        self.is_running = True

    def run(self) -> None:
        """run full game loop"""

        self.engine.start()

        while self.is_running:
            for event in self.engine.events:
                if event.type == QUIT:
                    self.is_running = False

            self.engine.update()

        self.engine.quit()
