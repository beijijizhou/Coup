from .character import Character
from typing import List
from .in_game_type import ActionType,TargetType,CharacterType
from .turn_data import BoardcastActionData
import random,time
class Player():
    _characters: List[Character] = [] * 2
    coins = 2
    message = ""
    type = ""  
    index = 0
    name = ""
    alive = True
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
        
        if isinstance(data, BoardcastActionData):
            current_player = data.current_player
            if current_player.index != self.index:
                if self.type == TargetType.AI:
                    pass
    def handle_boardcast_action_event(self,data):
        pass
    def select_ai_action_type():
        target_names = [member.name for member in CharacterType]
    #   time.sleep(1)
        return random.choice(target_names)