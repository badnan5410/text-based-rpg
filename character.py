from entity import Entity

class Character(Entity):

    def __init__(self, name, entity_type):
        super().__init__(name, entity_type)

class Player(Character):

    def __init__(self, name):
        super().__init__(name, entity_type="player")
        self.has_star = False
        self.inventory = []

    def interact_with(self, target):
        target.interact(self)

    def remove_item(self, target_name):
        if self.inventory:
            for item in self.inventory:
                if item.name == target_name:
                    self.inventory.remove(item)
                    break

    def check_inventory(self, target_name):
        if self.inventory:
            for item in self.inventory:
                if item.name == target_name:
                    return True
            return False
        else:
            return False


