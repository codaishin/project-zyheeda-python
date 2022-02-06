from config import SETTINGS
from core import Engine, Game

if __name__ == "__main__":
    engine = Engine(SETTINGS)
    game = Game(engine)
    game.run()
