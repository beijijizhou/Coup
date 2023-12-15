from .character import Character
from typing import List
from .in_game_type import ActionType,TargetType
from .turn_data import ActionData
class Player():
    _characters: List[Character] = [] * 2
    coins = 2
    message = ""
    type = ""  
    index = 0
    name = ""
    def __init__(self, characters:List[Character], record):
        self._characters = characters
        self.name = record['name']
        self.index = record['index']
        self.set_player_type()
    
    def set_player_type(self):
        if self.name[0] == 'P':
            self.type = TargetType.PLAYER
        else:
            self.type = TargetType.AI
    
    
    
    def _counter_or_challenge():
        pass
    def _counter(self):
        pass

    def _challenge(self):
        pass
    def get_characters(self):
        return self._characters

    def handle_event(self, data):
        
        print(isinstance(data, ActionData))
        pass
       
        