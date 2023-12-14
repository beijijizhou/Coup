from .player import Player
from .character import Character
from typing import List
import random


class GameManager:
    in_game = True
    _players: List[Player] = []
    
    _CARDS_NUMBER = 5
    
    _allowed_player_number = 6
    _current_player_number = 0
    def __init__(self, number):
        self._cards_pool = [0] * self._CARDS_NUMBER 
        self._players = [None] * number
        self._current_player_number = number
        self._init_cards_pool()
        self._generate_character_for_all_players()
   
    def run_game(self):
        pass
    def process_turn(self):
        if self.game_started:
            pass
    def _generate_character_for_all_players(self):
        for i in range(self._current_player_number):
            characters = []
            for j in range(2):
                # characters.append(Character(self._generate_index()))
                characters.append(Character(i))
            self._players[i] = Player(characters)
        
    
    def _generate_index(self):
        index = random.randint(0,4)
        while(self._cards_pool[index] < 1):
            index = random.randint(0,4)
        self._cards_pool[index] -= 1
        
        return index
    
    def _init_cards_pool(self):
        for i in range(self._CARDS_NUMBER):
            self._cards_pool[i] = 3
    
        
    def end_game(self):
        self.in_game = False