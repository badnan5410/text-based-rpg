from entity import Entity
from exceptions import GameMechanicError

class Item(Entity):

    def __init__(self, name, entity_type):
        super().__init__(name, entity_type)
        
class Key(Item):
    
    def __init__(self):
        super().__init__(name="key", entity_type="item")

class Star(Item):

    def __init__(self):
        super().__init__(name="star", entity_type="item")

    def interact(self, target):

        if target.entity_type == "player":
            print(f"\n>Congratulations {target.name}, you found the legendary star! You win the game!\n")
            target.inventory.append(self)
        else:
            raise GameMechanicError(f"\n>Error: Only entity type 'player' can interact with entity type '{self.entity_type}'.\n")