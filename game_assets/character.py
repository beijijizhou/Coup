from enum import Enum

class CharacterColor(Enum):
    Contessa = "red"
    Duke = "purple"
    Captain = "blue"
    Ambassador = "green"
    Assassin = "black"
class Character():
    character_candiates = ["Contessa","Duke", "Captain", "Ambassador", "Assassin"]
    character_color = ["red", "purple", "blue","green","black"]
    character_instances = {}
    alive = False
    def __init__(self, index):
       
        self._name = self.character_candiates[index]
        self._color = self.character_color[index]
       

        # character_class = character_classes.get(self.name)
        # if character_class:
        #         self.character_instances[self.name] = character_class(self.name)
    def action(self, coins):
        pass

 


        
            
