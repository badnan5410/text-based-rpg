from entity import Entity
from exceptions import GameMechanicError

class Object(Entity):

    def __init__(self, name, entity_type):
        super().__init__(name, entity_type)

class Chest(Object):

    def __init__(self, items):
        super().__init__(name="chest", entity_type="object")
        self.inventory = items

    def look_inside(self):
        if self.inventory:
            for item in self.inventory:
                return f"- {item.name}"
        else:
            return 'empty chest'

    def interact(self, target):
        if target.entity_type == "player":
            if self.inventory:
                print(f"\n>{target.name}, you look inside the {self.name} and you find:\n{self.look_inside()}")
                target.inventory.extend(self.inventory)
                self.inventory.clear()
            else:
                print(f"\n>{target.name}, this {self.name} is empty.\n")
        else:
            raise GameMechanicError(
                f"\n>Error: Only entity type 'player' can interact with entity type '{self.entity_type}'.\n")

class Door(Object):

    def __init__(self):
        super().__init__(name="door", entity_type="object")
        self.is_locked = True

    def check_for_key(self, target):
        if target.inventory:
            for item in target.inventory:
                if item.name == "key":
                    return True
            return False
        else:
            return False

    def interact(self, target):
        if target.entity_type == "player":
            if self.is_locked:
                if self.check_for_key(target):
                    print(f"\n>{target.name}, you use your key to unlock the {self.name}.\n")
                    target.remove_item("key")
                    self.is_locked = False
                    print(f"\n>{target.name}, you walk through the {self.name}.\n")
                else:
                    print(f"\n>{target.name}, you need a key to unlock this door.\n")
            else:
                print(f"\n>{target.name}, you walk through the {self.name}.\n")
        else:
            raise GameMechanicError(f"\n>Error: Only entity type 'player' can interact with entity type '{self.entity_type}'.\n")


