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
            self.character_action_details[character.name] = character.value

    def _show_general_actions(self):
        pass
    def set_shown(self):
        if self.shown:
            self.shown = False
    def handle_event(self, data):
        # self.shown = data.name[0] == 'P'
        pass
    def handle_boardcast_action_event(self,data):
        pass
        # current_player = 
        # if isinstance(data, TurnData):
        #     match data.action_type:
        #         case ActionType.START_TURN:
 
        #             self.message = data.name + " starts the turn."
        # else:
            
        #     match data.action_type:
        #         case ActionType.PENDING_ACTION:
        #             self.message = (
        #                 f"{data.name} selected the action \n"
        #                 f"{data.player_action_type}: {CharacterType[data.player_action_type].value}\n"
        #             )
                    
                  
