


class TurnData():
    def __init__(self, action_type, index=-1, action = None, target_index=None, 
                target_type=None, message=None, name=None):
        self.action_type = action_type
        self.action = action
        self.index = index
        self.target_index = target_index
        self.target_type = target_type
        self.name = name
class ActionData():
    def __init__(self, message_action_type, player_action_type, index, name ):
        self.message_action_type = message_action_type
        self.index = index
        self.player_action_type = player_action_type
        self.name = name
