from .player import Player
from .character import Character
from typing import List
import random
from .event_queue import EventQueue
from .in_game_type import ActionType
from .turn_data import TurnData
from .action_display import ActionDisplay
class GameManager():
    in_game = True
    _players: List[Player] = []

    _CARDS_NUMBER = 5
    _allowed_player_number = 6
    _current_player_number = 0
    current_player_index = 0

    event_queue = None
    message = ""
    action_choices = ["",]

    def __init__(self, number):
        self._cards_pool = [0] * self._CARDS_NUMBER
        self._players = [None] * number
        self._current_player_number = number
        self._init_cards_pool()

        self.event_queue = EventQueue()
        self.action_display = ActionDisplay()
        
        self.run_game()
    
    def run_game(self):
        self.event_queue.subscribe(self)
        self._generate_character_for_all_players()
        self.process_turn(0)
        # print(self.action_display)
        pass

    def process_turn(self,index):
        
        self.event_queue.notify(TurnData(ActionType.START_TURN, index))
       
        # recei

    def _generate_character_for_all_players(self):
        for i in range(self._current_player_number):
            characters = []
            for j in range(2):
                # characters.append(Character(self._generate_index()))
                characters.append(Character(i))
            name= "player 1" if i == 0 else f"AI    {i}"
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
   
    def display_message(self):
        pass
    def handle_event(self, data: TurnData):
        match data.action_type:
            case ActionType.START_TURN:
                self.message = self._players[data.index].name  + " starts the turn"
    
    
    
   
