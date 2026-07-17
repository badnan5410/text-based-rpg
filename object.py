from entity import Entity
from exceptions import GameMechanicError

class Object(Entity):

    def __init__(self, name, entity_type):
        super().__init__(name, entity_type)

class Chest(Object):

    def __init__(self):
        super().__init__(name="chest", entity_type="object")
        self.is_empty = False

    def interact(self, target):
        if target.entity_type == "player":
            if not self.is_empty:
                print(f"\n>{target.name}, you look inside the {self.name} and you find a key!\n")
                target.has_key = True
                self.is_empty = True
            else:
                print(f"\n>{target.name}, this {self.name} is empty.\n")
        else:
            raise GameMechanicError(
                f"\n>Error: Only entity type 'player' can interact with entity type '{self.entity_type}'.\n")

class Door(Object):

    def __init__(self):
        super().__init__(name="door", entity_type="object")
        self.is_locked = True

    def interact(self, target):
        if target.entity_type == "player":
            if self.is_locked:
                if target.has_key:
                    print(f"\n>{target.name}, you use your key to unlock the {self.name}.\n")
                    target.has_key = False
                    self.is_locked = False
                    print(f"\n>{target.name}, you walk through the {self.name}.\n")
                else:
                    print(f"\n>{target.name}, you need a key to unlock this door.\n")
            else:
                print(f"\n>{target.name}, you walk through the {self.name}.\n")
        else:
            raise GameMechanicError(f"\n>Error: Only entity type 'player' can interact with entity type '{self.entity_type}'.\n")

class Star(Object):

    def __init__(self):
        super().__init__(name="star", entity_type="object")

    def interact(self, target):

        if target.entity_type == "player":
            print(f"\n>Congratulations {target.name}, you found the legendary star! You win the game!\n")
            target.has_star = True
        else:
            raise GameMechanicError(f"\n>Error: Only entity type 'player' can interact with entity type '{self.entity_type}'.\n")