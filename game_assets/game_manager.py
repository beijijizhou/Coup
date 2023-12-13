class GameManager:
    
    def __init__(self):
        # Initialize game-related variables and logic here
        self.game_started = False

    def start_game(self):
        self.game_started = True


    def process_turn(self):
        if self.game_started:
            pass