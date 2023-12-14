from .character import Character
from typing import List
class Player():
    _characters: List[Character] = [] * 2
    coins = 2
    def __init__(self, characters:List[Character], record):
        self._characters = characters
        print(record)
        self.name = record['name']
        self.index = record['index']

    def _start_turn(self):
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

    def handle_event(self, data):
        pass