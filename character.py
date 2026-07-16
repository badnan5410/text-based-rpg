from entity import Entity

class Character(Entity):

    def __init__(self, name, entity_type):
        super().__init__(name, entity_type)

class Player(Character):

    def __init__(self, name):
        super().__init__(name, entity_type="player")
        self.has_key = False