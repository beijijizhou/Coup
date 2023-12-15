from .turn_data import BoardcastActionData


class EventQueue():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.subscribers = []  # Initialize the subscribers list
        return cls._instance

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def boardcast(self, data):
        if isinstance(data, BoardcastActionData):
            self.boardcast_action_event(data)
     
     
    def boardcast_action_event(self,data):
        current_index = data.current_player.index
        print(current_index)
        print("")
        next_index = self.select_subscriber_index(current_index)
        while next_index != current_index :
            print(next_index)
            self.subscribers[next_index].handle_boardcast_action_event(data)
            next_index = self.select_subscriber_index(next_index)
            
    
    def select_subscriber_index(self,i):
        if(i == len(self.subscribers) - 3):
            return 0
        return i + 1
