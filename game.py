from src.game_master import GameMaster
from loguru import logger

def main():
    game = GameMaster()
    game.init_game()
    game.play_game()

if __name__ == "__main__":
    main()