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
    def __init__(self, engine: EngineProtocol) -> None:
        self._engine = engine

    def _handle_events(self) -> bool:
        for event in self._engine.events:
            if event.type == QUIT:
                return False
        return True

    def run(self) -> None:
        self._engine.start()
        while self._handle_events():
            self._engine.update()
        self._engine.quit()
