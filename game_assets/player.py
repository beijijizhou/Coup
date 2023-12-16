from .character import Character
from typing import List
from .in_game_type import ActionType, TargetType, CharacterActions, CounterActions, ChallengeActions, CounterRelation
from .turn_data import BoardcastActionData
import random
import time


class Player():
    characters: List[Character] = [] * 2
    coins = 2
    player_type = ""
    index = 0
    name = ""
    
    current_action = ""
    current_character = ""
    influence = 0

    def __init__(self, characters: List[Character], record):
        self.characters = characters
        self.name = record['name']
        self.index = record['index']
        self.set_player_type()
        self.current_action_messages = []
        self.alive = True
    def set_player_type(self):
        if self.name[0] == 'P':
            self.player_type = TargetType.PLAYER
        else:
            self.player_type = TargetType.AI

    def handle_counteract(self):

        return self.select_ai_action(ActionType.CHALLENGE)

    def handle_challenge_result(self, result):
        if result:
            self.current_action_messages.append(self.name + " won the challenge") 
        else:
            self.current_action_messages.append(self.name + " lost the challenge and one influence") 

        # if not result:
        #     if(self.influence <= 1):
        #         self.characters[self.influence].alive = False
        #         self.influence += 1
        #     if self.influence == 2:
        #         self.alive = False

    def handle_event(self, data):
        pass

    def handle_boardcast_action_event(self, data):
        player_action_type = data.player_action_type
        if (self.player_type == TargetType.AI ):
            return self.select_ai_action(ActionType.COUNTERACT)
        # else:
        #     return self.set_current_action(player_action_type)

    def select_ai_action(self, action_type):
        current_action = ""
        match action_type:

            case ActionType.START_TURN:
                current_action = self.random_ai_actions(CharacterActions)
            case ActionType.COUNTERACT:
                # current_action = self.random_ai_actions(CounterActions)
                current_action = CounterActions.CHALLENGE
            case ActionType.CHALLENGE:
                current_action = self.random_ai_actions(ChallengeActions)

        return self.set_current_action(current_action)

    def set_current_action(self, current_action):
        new_message = self.player_type.value + "      " + \
            str(self.index) + " decides to " + str(current_action.value) + "\n"
        
        self.current_action_messages.append(new_message)
        
        self.current_action = current_action
        self.current_character = current_action
        return self

    def random_ai_actions(self, actions):
        return random.choice([member for member in actions])
