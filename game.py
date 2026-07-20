import character, item, object

class Game:
    FOREST_ROOM = 0
    CAVE_ROOM = 1
    HUT_ROOM = 2

    def __init__(self):
        self.player = character.Player()
        self.chest = object.Chest([item.Key()])
        self.door = object.Door()
        self.star = item.Star()
        self.current_room = self.FOREST_ROOM

    def valid_user_choice(self, prompt, valid_choices):
        while True:
            user_choice = input(
                f"\n>{self.player.name}, {prompt}: "
            ).strip().lower()

            if user_choice not in valid_choices:
                print("\n>Invalid choice. Please pick again.\n")
            else:
                return user_choice

    def forest_room(self):
        if not self.player.check_inventory("key"):
            print(
                f"\n>{self.player.name}, you find yourself inside a mysterious forest. "
                f"You see two paths in front of you. The path to the right leads "
                f"to a dark cave. The path to your left leads to a mysterious hut. "
                f"Which path will you take?\n"
            )

            choice = self.valid_user_choice(
                "press [A] to explore the cave. Press [B] to go to the hut",
                ["a", "b"]
            )

            if choice == "a":
                print(
                    f"\n>{self.player.name}, you decide to explore the cave...\n"
                )
                return self.CAVE_ROOM
            else:
                print(
                    f"\n>{self.player.name}, you decide to go to the hut...\n"
                )
                return self.HUT_ROOM

        else:
            print(
                f"\n>{self.player.name}, you are back in the forest. Now that you "
                f"have a key, I wonder what it unlocks?\n"
            )

            choice = self.valid_user_choice(
                "press [A] to go back to the cave. Press [B] to go to the hut",
                ["a", "b"]
            )

            if choice == "a":
                print(
                    f"\n>{self.player.name}, you decide to go back to the cave...\n"
                )
                return self.CAVE_ROOM
            else:
                print(
                    f"\n>{self.player.name}, you decide to go to the hut...\n"
                )
                return self.HUT_ROOM

    def cave_room(self):
        if not self.player.check_inventory("key"):
            print(
                f"\n>{self.player.name}, you find yourself inside a dark cave. "
                f"Inside, you find an old chest. Perhaps it contains treasure? "
                f"{self.player.name}, do you dare look inside?\n"
            )

            choice = self.valid_user_choice(
                "press [A] to look inside the chest. Press [B] to leave the cave",
                ["a", "b"]
            )

            if choice == "a":
                print(
                    f"\n>{self.player.name}, you decide to look inside the chest...\n"
                )
                self.player.interact_with(self.chest)
                return self.CAVE_ROOM
            else:
                print(
                    f"\n>{self.player.name}, you decide to leave the cave...\n"
                )
                return self.FOREST_ROOM

        else:
            print(
                f"\n>{self.player.name}, there doesn't seem to be anything else here. "
                f"Maybe you should check out that hut?\n"
            )

            choice = self.valid_user_choice(
                "press [A] to look inside the chest again. "
                "Press [B] to leave the cave",
                ["a", "b"]
            )

            if choice == "a":
                print(
                    f"\n>{self.player.name}, you decide to look inside the chest again...\n"
                )
                self.player.interact_with(self.chest)
                return self.CAVE_ROOM
            else:
                print(
                    f"\n>{self.player.name}, you decide to leave the cave...\n"
                )
                return self.FOREST_ROOM

    def hut_room(self):
        if not self.player.check_inventory("key"):
            print(
                f"\n>{self.player.name}, you arrive at the mysterious hut, but the "
                f"door seems to be locked. I wonder what's behind it?\n"
            )

            choice = self.valid_user_choice(
                "press [A] to try to open the door. Press [B] to leave the hut",
                ["a", "b"]
            )

            if choice == "a":
                print(
                    f"\n>{self.player.name}, you try to open the door...\n"
                )
                self.player.interact_with(self.door)
                return self.HUT_ROOM
            else:
                print(
                    f"\n>{self.player.name}, you decide to leave the hut...\n"
                )
                return self.FOREST_ROOM

        else:
            print(
                f"\n>{self.player.name}, you arrive at the mysterious hut, but the "
                f"door seems to be locked. I wonder what's behind it?\n"
            )

            choice = self.valid_user_choice(
                "press [A] to unlock the door with your key. "
                "Press [B] to leave the hut",
                ["a", "b"]
            )

            if choice == "a":
                print(
                    f"\n>{self.player.name}, you try unlocking the door with your key...\n"
                )
                self.player.interact_with(self.door)

                print(
                    f"\n>{self.player.name}, inside the hut, you find the most "
                    f"beautiful treasure in the world.\n"
                )
                self.player.interact_with(self.star)

                return self.HUT_ROOM
            else:
                print(
                    f"\n>{self.player.name}, you decide to leave the hut...\n"
                )
                return self.FOREST_ROOM

    def update_room(self):
        match self.current_room:
            case 0:
                return self.forest_room()
            case 1:
                return self.cave_room()
            case 2:
                return self.hut_room()
            case _:
                return None

    def start(self):

        while True:
            self.current_room = self.update_room()

            if self.current_room == self.HUT_ROOM and self.player.check_inventory("star"):
                break

