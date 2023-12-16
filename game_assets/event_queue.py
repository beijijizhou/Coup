from .turn_data import BoardcastActionData
from typing import List
from .player import Player
from .in_game_type import CounterActions, ActionType


class EventQueue():
    _instance = None
    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         cls._instance.subscribers = []  # Initialize the subscribers list
    #     return cls._instance
    def __init__(self) -> None:
        self.subscribers: List[Player] = []
        self.current_player: Player
        self.current_responding_player: Player
        self.other_players: List[Player] = []
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def boardcast(self, data):
        self.current_player = data.current_player
        if isinstance(data, BoardcastActionData):
            return self.boardcast_action_event(data)

    def boardcast_action_event(self, data):
        current_index = data.current_player.index
        next_index = self.select_subscriber_index(current_index)
        while next_index != current_index:
            self.responding_player = self.subscribers[next_index].handle_boardcast_action_event(
                data)
            
            self.other_players.append(self.responding_player)
            self.handle_boardcast_current_action()
            if(not self.current_player.alive):
                return 
            next_index = self.select_subscriber_index(next_index)
        
    def handle_boardcast_current_action(self):

        match self.responding_player.current_action:
            case CounterActions.COUNTERACT:
                self.send_counteract_event()
            case CounterActions.CHALLENGE:
                self.handle_challenge_event()
            case CounterActions.IGNORE:
                pass

    def send_counteract_event(self):
        self.current_player.handle_counteract()

    def handle_challenge_event(self):
        self.send_challenge_result(
            self.current_player.current_character in self.current_player.characters)

    def send_challenge_result(self, result):
        self.current_player.handle_challenge_result(result)
        self.responding_player.handle_challenge_result(not result)

    def select_subscriber_index(self, i):
        if (i == len(self.subscribers) - 3):
            return 0
        return i + 1
