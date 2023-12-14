from .character import Character
from typing import List
from .turn_data import TurnData
from .in_game_type import ActionType

class Player():
    _characters: List[Character] = [] * 2
    coins = 2
    message = ""
    def __init__(self, characters:List[Character], record):
        self._characters = characters
        self.name = record['name']
        self.index = record['index']
        

    def _start_turn(self):
        # message = self.name + " is playing the turn"
        self._show_all_actions()
        
   

    def _show_all_actions(self):
        self._show_general_actions()
        self._show_character_actions()
        pass

    def _show_character_actions(self):
        pass

    def _show_general_actions(self):
        pass

    def _counter_or_challenge():
        pass
    def _counter(self):
        pass

    def _challenge(self):
        pass
    def get_characters(self):
        return self._characters

    def handle_event(self, data: TurnData):
        if(self.index == data.index):
            match data.action_type:
                case ActionType.START_TURN:
                    self._start_turn()


        pass