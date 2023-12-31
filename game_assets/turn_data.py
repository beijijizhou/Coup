class TurnData():
    def __init__(self, action_type, index=-1, action=None, target_index=None,
                 target_type=None, message=None, name=None):
        self.action_type = action_type
        self.action = action
        self.index = index
        self.target_index = target_index
        self.target_type = target_type
        self.name = name


class BoardcastActionData():
    def __init__(self, action_type, player_action_type, player_type, current_player):
        self.action_type = action_type
        self.player_action_type = player_action_type
        self.player_type = player_type
        self.current_player = current_player
