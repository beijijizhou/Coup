class EventQueue():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.subscribers = []  # Initialize the subscribers list
        return cls._instance

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
       
    def notify(self, data):
        for player in self.subscribers:
            player.handle_event(data)


