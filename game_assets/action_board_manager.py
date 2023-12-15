from game_assets.in_game_type import ActionBoardState, CharacterType, CounterActions, ChallengeActions, OtherPlayerTurn


class ActionBoardManager():
    action_board_state = None
    action_board_details = None

    def __init__(self) -> None:
        self.set_action_board(ActionBoardState.PLAYER_TURN)

    def set_action_board(self, state) -> None:
        self.action_board_state = state
        match state:
            case ActionBoardState.PLAYER_TURN:
                self.action_board_details = CharacterType
            case ActionBoardState.COUNTER_ACTION:
                self.action_board_details = CounterActions
            case ActionBoardState.CHALLENGE:
                self.action_board_details = ChallengeActions
            case ActionBoardState.OTHER_PLAYER_TURN:
                self.action_board_details = OtherPlayerTurn
