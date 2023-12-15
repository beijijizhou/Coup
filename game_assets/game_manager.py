from .player import Player
from .character import Character
from typing import List
import random
from .event_queue import EventQueue
from .in_game_type import ActionType, CharacterType
from . import in_game_type
from .action_board_manager import ActionBoardManager
from .turn_data import TurnData, BoardcastActionData
from .action_display import ActionDisplay


class GameManager():
    in_game = True
    players: List[Player] = []

    _CARDS_NUMBER = 5
    _allowed_player_number = 6
    _current_player_number = 0
    current_player_index = 0
    current_player: Player

    event_queue = None
    message = ""
    in_game_type = in_game_type

    def __init__(self, number):
        self._cards_pool = [0] * self._CARDS_NUMBER
        self.players = [None] * number
        self._current_player_number = number
        self._init_cards_pool()

        self.event_queue = EventQueue()
        self.action_display = ActionDisplay()
        self.action_board_manager = ActionBoardManager()
        self.run_game()

    def run_game(self):
        self._generate_character_for_all_players()
        self.subscribe()
        self.process_turn()

    def subscribe(self):
        self.event_queue.subscribe(self)
        self.event_queue.subscribe(self.action_display)

    def process_turn(self):
        self.current_player = self.players[self.current_player_index]
        # self.event_queue.notify(TurnData(ActionType.START_TURN,  ))

        # recei

    def _generate_character_for_all_players(self):
        for i in range(self._current_player_number):
            characters = []
            for j in range(2):
                # characters.append(Character(self._generate_index()))
                characters.append(Character(i))
            name = "Player 1" if i == 0 else f"AI    {i}"
            record = {
                'name': name,
                'index': i
            }
            self.players[i] = Player(characters, record)
            self.event_queue.subscribe(self.players[i])

    def _generate_index(self):
        index = random.randint(0, 4)
        while (self._cards_pool[index] < 1):
            index = random.randint(0, 4)
        self._cards_pool[index] -= 1

        return index

    def _init_cards_pool(self):
        for i in range(self._CARDS_NUMBER):
            self._cards_pool[i] = 3

    def player_selected_action(self, player_action_type, player_type):
        self.event_queue.boardcast(BoardcastActionData(
            ActionType.PENDING_ACTION, player_action_type, self.current_player))
        return "hah"
        # self.end_turn()

    def end_turn(self):
        self.current_player_index += 1
        self.process_turn()
    def handle_boardcast_action_event(self,data):
        pass
    def handle_event(self, data):
        pass
        # match data.action_type:
        #     case ActionType.START_TURN:
        #         self.message = self._players[data.index].name  + " starts the turn"
