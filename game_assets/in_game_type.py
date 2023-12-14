from enum import Enum

class ActionType(Enum):
    START_TURN = 1
    END_TURN = 2
    CHARACTER_ACTION = 3
    GENERAL_ACTION = 4
    CHALLENGE = 5
    COUNTERACT = 6
    NOTIFY = 7

class TargetType(Enum):
    GAME_MANAGER = 1
    PARTICIPANT = 2
    PLAYER = 3
    AI = 4
    TREASURY = 5
    DECK = 6


class CharacterType(Enum):
    DUKE = "Duke - Tax\nTake 3 coins from the Treasury."
    ASSASSIN = "Assassin - Assassinate\nPay 3 coins to the Treasury and launch an assassination against another player. If successful that player immediately loses an influence. (Can be blocked by the Contessa)"
    CAPTAIN = "Captain - Steal\nTake 2 coins from another player. If they only have one coin, take only one. (Can be blocked by the Ambassador or the Captain)"
    AMBASSADOR = "Ambassador - Exchange\nExchange cards with the Court. First take 2 random cards from the Court deck. Choose which, if any, to exchange with your face-down cards. Then return two cards to the Court deck."

    