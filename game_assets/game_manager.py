from .player import Player
from .character import Character
from typing import List
import random
from .event_queue import EventQueue
from .in_game_type import ActionType, CharacterType
from .turn_data import TurnData, ActionData
from .action_display import ActionDisplay
class GameManager():
    in_game = True
    _players: List[Player] = []

    _CARDS_NUMBER = 5
    _allowed_player_number = 6
    _current_player_number = 0
    current_player_index = 1
    current_player_name = ""

    event_queue = None
    message = ""
    

    def __init__(self, number):
        self._cards_pool = [0] * self._CARDS_NUMBER
        self._players = [None] * number
        self._current_player_number = number
        self._init_cards_pool()
        self.event_queue = EventQueue()
        self.action_display = ActionDisplay()
        
        self.run_game()
    
    def run_game(self):
        
        self.subscribe()
        self._generate_character_for_all_players()
        self.process_turn()

    def subscribe(self):
        self.event_queue.subscribe(self)
        self.event_queue.subscribe(self.action_display)

    def process_turn(self):
        self.current_player_name = self._players[self.current_player_index].name
        self.event_queue.notify(TurnData(ActionType.START_TURN, self.current_player_index, name = self.current_player_name ))
       
        # recei

    def _generate_character_for_all_players(self):
        for i in range(self._current_player_number):
            characters = []
            for j in range(2):
                # characters.append(Character(self._generate_index()))
                characters.append(Character(i))
            name= "Player 1" if i == 0 else f"AI    {i}"
            record = {
                'name': name,
                'index' : i
            }
            self._players[i] = Player(characters, record)
            self.event_queue.subscribe(self._players[i])
        
    def _generate_index(self):
        index = random.randint(0, 4)
        while (self._cards_pool[index] < 1):
            index = random.randint(0, 4)
        self._cards_pool[index] -= 1

        return index

    def _init_cards_pool(self):
        for i in range(self._CARDS_NUMBER):
            self._cards_pool[i] = 3

    def get_players(self):
        return self._players
   

    def player_selected_action(self, player_action_type):
        self.event_queue.notify(ActionData(ActionType.PENDING_ACTION, player_action_type,
        self.current_player_index, self.current_player_name))
        print(player_action_type)
        # self.end_turn()
    
    def end_turn(self):
        self.current_player_index += 1
        self.process_turn()
       
    def handle_event(self, data: TurnData):
        pass
        # match data.action_type:
        #     case ActionType.START_TURN:
        #         self.message = self._players[data.index].name  + " starts the turn"
    
    
    
   
