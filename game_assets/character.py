# from .game_characters.duke import Duke

# character_classes = {
#     "Duke": Duke,
# }
class Character:
    character_candiates = ["Contessa","Duke", "Captain", "Ambassador", "Assassin"]
    character_color = ["red", "purple", "blue","green","black"]
    character_instances = {}
    def __init__(self, index):
       
        self._name = self.character_candiates[index]
        self._color = self.character_color[index]
        print(self._color)
        print(self._name)
        # print(index)
        # print(self.name)
        # character_class = character_classes.get(self.name)
        # if character_class:
        #         self.character_instances[self.name] = character_class(self.name)
    def action(self, coins):
        pass
    
        
            
