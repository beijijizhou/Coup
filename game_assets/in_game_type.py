from enum import Enum


class ActionType(Enum):
    START_TURN = 1
    END_TURN = 2
    CHARACTER_ACTION = 3
    GENERAL_ACTION = 4
    CHALLENGE = 5
    COUNTERACT = 6
    NOTIFY = 7
    PENDING_ACTION = 8
    FOREIGN_AID = 9


class EventQueueStatus(Enum):
    IDLE = 1
    WORKING = 2
    WAIT_FOR_HUMAN_COUNTERACT = 3


class GeneralActions(Enum):
    INCOME = "Income: Take 1 coin from the Treasury."
    FOREIGN_AID = "Foreign Aid: Take 2 coins from the Treasury. (Can be blocked by the Duke)"
    COUP = "Coup: Pay 7 coins to the Treasury and launch a Coup against another player. That player immediately loses an influence. A Coup is always successful. If you start your turn with 10 (or more) coins you are required to launch a Coup."


class CounterActions(Enum):
    COUNTERACT = "Counteract current player's action"
    CHALLENGE = "Challenge current player"
    IGNORE = "Permit current player's action"


class ChallengeActions(Enum):
    CHALLENGE = "Challenge current player"
    IGNORE = "Permit current player's action"


class TargetType(Enum):
    GAME_MANAGER = "game_manager"
    PLAYER = "player"
    AI = "ai"
    TREASURY = "treasury"
    DECKER = "decker"


class CharacterActions(Enum):
    DUKE = "Duke - Tax\nTake 3 coins from the Treasury."
    ASSASSIN = "Assassin - Assassinate\nPay 3 coins to the Treasury and launch an assassination against another player. If successful that player immediately loses an influence. (Can be blocked by the Contessa)"
    CAPTAIN = "Captain - Steal\nTake 2 coins from another player. If they only have one coin, take only one. (Can be blocked by the Ambassador or the Captain)"
    AMBASSADOR = "Ambassador - Exchange\nExchange cards with the Court. First take 2 random cards from the Court deck. Choose which, if any, to exchange with your face-down cards. Then return two cards to the Court deck."


class CharacterColor(Enum):
    CONTESSA = "red"
    DUKE = "purple"
    CAPTAIN = "blue"
    AMBASSADOR = "green"
    ASSASSIN = "black"


class ActionBoardState(Enum):
    PLAYER_TURN = 1
    COUNTER_ACTION = 2
    CHALLENGE = 3
    OTHER_PLAYER_TURN = 4


class OtherPlayerTurn(Enum):
    Message = "Wait for action"


class CounterRelation(Enum):
    ASSASSIN = "CONTESSA"
    AMBASSADOR = "CAPTAIN"
    CAPTAIN = "CAPTAIN"
    DUKE = "FOREIGN_AID"


class GameStatus(Enum):
    GAME_OVER = "You lose the game, try again"
    WIN = "Congratulations"
    IN_GAME = "In game"
    NOT_STARTED = "Click to start"
    WAIT_FOR_HUMAN_COUNTERACT = 3

