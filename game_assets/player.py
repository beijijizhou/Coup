from .character import Character
from typing import List
from .in_game_type import ActionType, TargetType, CharacterActions, CounterActions, ChallengeActions, CounterRelation
from .turn_data import BoardcastActionData
import random
import time


class Player():
    characters: List[Character] = [] * 2
    coins = 2
    message = ""
    player_type = ""
    index = 0
    name = ""
    alive = True
    response = ""
    current_character = ""
    influence = 0
    
    
    def __init__(self, characters: List[Character], record):
        self.characters = characters
        self.name = record['name']
        self.index = record['index']
        self.set_player_type()

    def set_player_type(self):
        if self.name[0] == 'P':
            self.player_type = TargetType.PLAYER
        else:
            self.player_type = TargetType.AI

    def handle_counteract(self):

        return self.select_ai_action(ActionType.CHALLENGE)

    def handle_challenge_result(self,result):
        if not result:
            if(self.influence <= 1):
                self.characters[self.influence].alive = False
                self.influence += 1
            if self.influence == 2:
                self.alive = False
            


    def handle_event(self, data):
        pass

    def handle_boardcast_action_event(self, data):
        if (self.player_type == TargetType.AI):
            return self.select_ai_action(ActionType.COUNTERACT)

    def select_ai_action(self, action_type):
        response = ""
        match action_type:

            case ActionType.START_TURN:
                response = self.random_ai_actions(CharacterActions)
            case ActionType.COUNTERACT:
                # response = self.random_ai_actions(CounterActions)
                response = CounterActions.CHALLENGE
            case ActionType.CHALLENGE:
                response = self.random_ai_actions(ChallengeActions)
        print(self.player_type.value + "    " + str(self.index)+ "    "+ str(response))
        self.response = response
        self.current_character = response
        return self

    def random_ai_actions(self, actions):
        return random.choice([member for member in actions])
