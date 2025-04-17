from src.game_master import GameMaster
from loguru import logger

def main():
    print("Welcome to the Guerilla Card Game!")
    
    num_players = int(input("Choose the number of players 2-8"))

    while num_players > 8 or num_players < 2:
        logger.error("Error : Choose a right number of players ")

    gm = GameMaster(num_players)

    gm.start_game()

if __name__ == "__main__":
    main()