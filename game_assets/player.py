from .character import Character
from typing import List
from .turn_data import TurnData,ActionData
from .in_game_type import ActionType

class Player():
    _characters: List[Character] = [] * 2
    coins = 2
    message = ""
    def __init__(self, characters:List[Character], record):
        self._characters = characters
        self.name = record['name']
        self.index = record['index']
        
    def _counter_or_challenge():
        pass
    def _counter(self):
        pass

    def _challenge(self):
        pass
    def get_characters(self):
        return self._characters

    def handle_event(self, data):
        # print(isinstance(data, ActionType))
        if isinstance(data, ActionData):
            match data.message_action_type:
                case ActionType.PENDING_ACTION:
                    if(self.index != data.index):
                        pass
       
        