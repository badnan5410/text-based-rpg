from entity import Entity

class Character(Entity):

    def __init__(self, name, entity_type):
        super().__init__(name, entity_type)


def create_player():
    print("""
                ******************
                RPG TEXT ADVENTURE
                ******************
        \n\n""")

    while True:
        player_name = input("\n>Enter your name: ").strip()

        if not player_name.isalpha():
            print(f"\n>'{player_name}' is not a valid name. Please try again.\n")
        else:
            print(f"\n>Welcome, player {player_name}!\n")
            break

    return player_name


class Player(Character):

    def __init__(self):
        super().__init__(name=create_player(), entity_type="player")
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


