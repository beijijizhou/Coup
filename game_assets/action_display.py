from .in_game_type import CharacterType, ActionType
from .turn_data import TurnData


class ActionDisplay():
    message = ""
  
    def __init__(self):
        self.character_action_details = {}
        self.character_color_details = {}
        self._show_all_actions()
        self.shown = True
    def _show_all_actions(self):
        self._show_general_actions()
        self._show_character_actions()
        
    def _show_character_actions(self):
        for character in CharacterType:
            # self.character_color_details[character.name] = CharacterType[]
            self.character_action_details[character.name] = character.value
        # print(self.character_action_details)

    def _show_general_actions(self):
        pass
    def set_shown(self):
        if self.shown:
            self.shown = False
    def handle_event(self, data):
        self.shown = data.name[0] == 'P'
        
        if isinstance(data, TurnData):
            match data.action_type:
                case ActionType.START_TURN:
                    # print(data.name)
                    self.message = data.name + " starts the turn."
        else:
            print(CharacterType[data.player_action_type].value)
            match data.message_action_type:
                case ActionType.PENDING_ACTION:
                    self.message = (
                        f"{data.name} selected the action \n"
                        f"{data.player_action_type}: {CharacterType[data.player_action_type].value}\n"
                        
                    )
                    # print(data.player_action_type)
                    # print(CharacterType[data.player_action_type].value)
