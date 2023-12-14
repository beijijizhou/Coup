from .in_game_type import CharacterType
class ActionDisplay():

    def __init__(self):
        self.character_action_details = {}
        self._show_all_actions()
    
    def _show_all_actions(self):
        self._show_general_actions()
        self._show_character_actions()
        

    def _show_character_actions(self):
        for character in CharacterType:
            self.character_action_details[character.name] = character.value
        # print(self.character_action_details)
        

    def _show_general_actions(self):
        pass