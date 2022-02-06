from test import UnitTests
from typing import Iterable
from unittest.mock import Mock, call

from pygame import QUIT
from pygame.event import Event

from ..game import Game


class TestGame(UnitTests):
    class Engine(Mock):
        mock_events: list[Iterable[Event]] = []

        def pull_events(self) -> Iterable[Event]:
            return self.mock_events.pop(0)


@TestGame.describe("run: start -> quit")
def _(test: TestGame) -> None:
    engine = test.Engine(mock_events=[[Mock(type=QUIT)]])
    game = Game(engine)

    game.run()

    engine.assert_has_calls((call.start(), call.quit()))


@TestGame.describe("run: start -> update -> quit")
def _(test: TestGame) -> None:
    engine = test.Engine(mock_events=[[], [Mock(type=QUIT)]])
    game = Game(engine)

    game.run()

    engine.assert_has_calls((call.start(), call.update(), call.quit()))


@TestGame.describe("run: start -> update -> update -> quit")
def _(test: TestGame) -> None:
    engine = test.Engine(mock_events=[[], [Mock()], [Mock(type=QUIT)]])
    game = Game(engine)

    game.run()

    engine.assert_has_calls(
        (call.start(), call.update(), call.update(), call.quit())
    )
