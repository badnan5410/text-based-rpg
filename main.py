import character, object, item

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

def valid_user_choice(prompt, valid_choices):
    while True:
        user_choice = input(
            f"\n>{player.name}, {prompt}: "
        ).strip().lower()

        if user_choice not in valid_choices:
            print("\n>Invalid choice. Please pick again.\n")
        else:
            return user_choice

def forest_room():
    if not player.check_inventory("key"):
        print(
            f"\n>{player.name}, you find yourself inside a mysterious forest. "
            f"You see two paths in front of you. The path to the right leads "
            f"to a dark cave. The path to your left leads to a mysterious hut. "
            f"Which path will you take?\n"
        )

        choice = valid_user_choice(
            "press [A] to explore the cave. Press [B] to go to the hut",
            ["a", "b"]
        )

        if choice == "a":
            print(
                f"\n>{player.name}, you decide to explore the cave...\n"
            )
            return CAVE_ROOM
        else:
            print(
                f"\n>{player.name}, you decide to go to the hut...\n"
            )
            return HUT_ROOM

    else:
        print(
            f"\n>{player.name}, you are back in the forest. Now that you "
            f"have a key, I wonder what it unlocks?\n"
        )

        choice = valid_user_choice(
            "press [A] to go back to the cave. Press [B] to go to the hut",
            ["a", "b"]
        )

        if choice == "a":
            print(
                f"\n>{player.name}, you decide to go back to the cave...\n"
            )
            return CAVE_ROOM
        else:
            print(
                f"\n>{player.name}, you decide to go to the hut...\n"
            )
            return HUT_ROOM

def cave_room():
    if not player.check_inventory("key"):
        print(
            f"\n>{player.name}, you find yourself inside a dark cave. "
            f"Inside, you find an old chest. Perhaps it contains treasure? "
            f"{player.name}, do you dare look inside?\n"
        )

        choice = valid_user_choice(
            "press [A] to look inside the chest. Press [B] to leave the cave",
            ["a", "b"]
        )

        if choice == "a":
            print(
                f"\n>{player.name}, you decide to look inside the chest...\n"
            )
            player.interact_with(chest)
            return CAVE_ROOM
        else:
            print(
                f"\n>{player.name}, you decide to leave the cave...\n"
            )
            return FOREST_ROOM

    else:
        print(
            f"\n>{player.name}, there doesn't seem to be anything else here. "
            f"Maybe you should check out that hut?\n"
        )

        choice = valid_user_choice(
            "press [A] to look inside the chest again. "
            "Press [B] to leave the cave",
            ["a", "b"]
        )

        if choice == "a":
            print(
                f"\n>{player.name}, you decide to look inside the chest again...\n"
            )
            player.interact_with(chest)
            return CAVE_ROOM
        else:
            print(
                f"\n>{player.name}, you decide to leave the cave...\n"
            )
            return FOREST_ROOM

def hut_room():
    if not player.check_inventory("key"):
        print(
            f"\n>{player.name}, you arrive at the mysterious hut, but the "
            f"door seems to be locked. I wonder what's behind it?\n"
        )

        choice = valid_user_choice(
            "press [A] to try to open the door. Press [B] to leave the hut",
            ["a", "b"]
        )

        if choice == "a":
            print(
                f"\n>{player.name}, you try to open the door...\n"
            )
            player.interact_with(door)
            return HUT_ROOM
        else:
            print(
                f"\n>{player.name}, you decide to leave the hut...\n"
            )
            return FOREST_ROOM

    else:
        print(
            f"\n>{player.name}, you arrive at the mysterious hut, but the "
            f"door seems to be locked. I wonder what's behind it?\n"
        )

        choice = valid_user_choice(
            "press [A] to unlock the door with your key. "
            "Press [B] to leave the hut",
            ["a", "b"]
        )

        if choice == "a":
            print(
                f"\n>{player.name}, you try unlocking the door with your key...\n"
            )
            player.interact_with(door)

            print(
                f"\n>{player.name}, inside the hut, you find the most "
                f"beautiful treasure in the world.\n"
            )
            player.interact_with(star)

            return HUT_ROOM
        else:
            print(
                f"\n>{player.name}, you decide to leave the hut...\n"
            )
            return FOREST_ROOM

def update_room(current_room):
    match current_room:
        case 0:
            new_room = forest_room()
        case 1:
            new_room = cave_room()
        case 2:
            new_room = hut_room()

    return new_room

def start_game():
    current_room = FOREST_ROOM

    while True:
        current_room = update_room(current_room)

        if current_room == HUT_ROOM and player.check_inventory("star"):
            break


def main():
    start_game()

# Rooms
FOREST_ROOM = 0
CAVE_ROOM = 1
HUT_ROOM = 2

# Entities
player = character.Player(create_player())
chest = object.Chest([item.Key()])
door = object.Door()
star = item.Star()

if __name__ == "__main__":
    main()