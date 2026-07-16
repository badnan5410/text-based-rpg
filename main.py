import character as ch, object as obj

class GameMechanicError(Exception):
    pass

def create_player():
    print("""
                ******************
                RPG TEXT ADVENTURE
                ******************
        \n\n""")

    while True:
        player_name = input("\n>Enter your name: ")

        if not player_name.isalpha() or len(player_name) < 1:
            print(f"\n>'{player_name}' is not a valid name. Please try again.\n")
        else:
            print(f"\n>Welcome, player {player_name}!\n")
            break

    return player_name

def start_game():

    #create entities
    player = ch.Player(create_player())
    chest = obj.Chest()
    door = obj.Door()
    star = obj.Star()

    #test the door when its locked
    door.interact(player) #should not allow as player doesn't have a key

    #open the chest
    chest.interact(player) #player finds key

    #try opening chest again
    chest.interact(player) #no key anymore, its empty

    #try the door again
    door.interact(player) #now should be unlocked and player walks through

    #collect the star
    star.interact(player) #player collects star and wins the game

def main():
    start_game()

if __name__ == "__main__":
    main()