#!/usr/bin/env python3
''' Alice Huh - RPG Game '''
import time


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      ask [helper]
    ''')

def showStatus():
    run = True
    """determine the current status of the player"""
    # print the player's current location
    print("--------------------------------------")
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)

    """check item in the room"""
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        # if the item is helper, print the option to ask quesiton. 
        if rooms[currentRoom]['item'] == "Helper":
            print('Your current options are...')
            print('ask ' + rooms[currentRoom]['item'])
            showOption(currentRoom)         
            del rooms[currentRoom]['item']   

        # if the item is monster, check if the player has either medicien or weapon in inventory 
        # if the player has medicine or weapon, player survives, if not, player lose the game 
        elif rooms[currentRoom]['item'] == "Monster":
            print("There is monster in this room! It's attacking you!! ")
            time.sleep(1)
            print(".......")
            time.sleep(1)
            if "medicine" in inventory:
                print("Thank God, you have medicine. You are healed from the attack")
                inventory.remove('medicine')
                print('Your current options are...')   
                showOption(currentRoom)     
            elif "weapon" in inventory:
                print("You got rid of the monster with the weapon!")
                inventory.remove("weapon")
                print('Your current options are...')
                showOption(currentRoom)
            else:
                time.sleep(1)
                print("Sorry, you lost the game")
                run = False
        # if the player meet Pete, save it in inventory, and remove Pete from the room. 
        elif rooms[currentRoom]['item'] == "Pete" and "Pete" not in inventory:
            print("You found PETE!! He will go with you from now on")
            inventory.append("Pete")
            print('Your current options are...')
            del rooms[currentRoom]['item']
            showOption(currentRoom)       
        # if the player found the secret door, display player's inventory and ask if player wants to leave now.
        elif rooms[currentRoom]['item'] == "secret door" :
            print("You found the Secret Door!")
            print(f"Here's your inventory : {inventory}")
            answer = input("Do you want to leave the house now? 1.Yes 2. No \n> " )
            
            # if the player select yes, check if key and pete are in the inventory.
            # if key and pete both are in inventory, player wins. if only key in inventory, user cannot leave. if only Pete in inventory, user lose.
            if answer.lower == "1" or "yes":
                if "key" and "Pete" in inventory:
                    print("You saved PETE!! YAY!")
                    run = False
                elif "Pete" in inventory: 
                    print("oh no, you don't have a key to open the door. Please, find the key!")
                elif "Key" in inventory:
                    print("You got out of the Monster's house, but your friend, Pete, is still waiting for you.. You lost the game")
            # if player select to keep playing, display the options 
            elif answer.lower == "2" or "no":
                print("Okay, now you know the secret door is in Music room. Let's keep on journey")
                showOption(currentRoom)
        
        # if the item is not a special item (pete, key, mosnter, secret door), save the item in inventory
        else:
            print('get ' + rooms[currentRoom]['item'])
            showOption(currentRoom)   
    
    # no item found in the room     
    else: 
        print('There is no item found in ' + currentRoom)
        print('Your current options are...')
        showOption(currentRoom)
    return run 


# show the rooms and direction user can go. 
def showOption(currentRoom):

    if "south" in rooms[currentRoom]:
        south = rooms[currentRoom]['south']
        print(f'go south: {south}')

    if "north" in rooms[currentRoom]:
        north = rooms[currentRoom]['north']
        print(f'go north: {north}')

    if "east" in rooms[currentRoom]:
        east = rooms[currentRoom]['east']
        print(f'go east: {east}')

    if "west" in rooms[currentRoom]:
        west = rooms[currentRoom]['west']
        print(f'go west: {west}')

    print("--------------------------------------")
    

#room dictionary 
rooms = {
    
    'hall' : {
        'south' : 'living room'
    },

    'living room' : {
        'south' : 'library',
        'east' : 'bathroom',
        'west' : 'kitchen',
        'north' : 'hall'
    },

    'library' : {
        'south' : 'powder room',
        'east' : 'study room',
        'west' : 'dining room',
        'north' : 'living room',
        'item' : 'Helper'
    },

    'powder room' : {
        'south': 'bedroom',
        'east' : 'guest room',
        'west' : 'garden',
        'north': 'library',
        'item' : 'weapon'
    },

    'bedroom' : {
        'east' : 'flex room',
        'west' : 'music room',
        'north': 'powder room',
        'item' : 'Monster'
    },

    'bathroom' : {
        'south': 'study room',
        'east' : 'living room',
        'item' : 'medicine' 
    },

    'study room' : {
        'south': 'garden',
        'east' : 'library',
        'north': 'bathroom',
        'item' : 'Pete'  
    },

    'garden' : {
        'south': 'flex room',
        'east' : 'powder room',
        'north': 'study room',
    },

    'flex room' : {
        'east' : 'bedroom',
        'north': 'garden',
        'item' : 'key'  
    },

    'kitchen' : {
        'south': 'dining room',
        'west' : 'living room',
        'item' : 'Helper'  
    },

    'dining room' : {
        'south': 'guest room',
        'west' : 'library',
        'north': 'kitchen',
        'item' : 'Monster'  
    },

    'guest room' : {
        'south': 'music room',
        'west' : 'powder room',
        'north': 'dining room'
        
    },


    'music room' : {
        'west' : 'bedroom',
        'north': 'guest room',
        'item' : 'secret door'  
    },

}

#player starts the game with 0 item in inventory 
inventory = []
# user starts the game from the hall 
currentRoom = 'hall'
# value changes if the player meet the helper. this prevents player to revisit the helper's room to get the help
kitchen_helper = False
library_helper = False


# game starts 
showInstructions()

# when the value changes to False, game ends. 
run = True

# breaking this while loop means the game is over
while run:
    run = showStatus()
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while run and move == '':  
        move = input('>')
        print()

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if user type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if user type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match

    #if user type 'ask' first    
    if move[0] == 'ask':
        valid_input = False
        # check if the player met the helper at the kitchen or library. 
        # check if the player already met the same helper before, and if so, player cannot meet the helper
        if currentRoom == 'kitchen' :
            if kitchen_helper == True:
                print("Helper is not in this room anymore")
                valid_input = True
            else:
                kitchen_helper = True 
        if currentRoom == 'library' :
            if library_helper == True:
                print("Helper is not in this rrom anymore")
                valid_input = True
            else:
                library_helper = True

        
        # make a list of rooms except the current room. This list will be displayed by helper for room choice. 
        display_room = []
        for i in rooms:
            if rooms[i] != currentRoom:
                display_room.append(i)
            
        # helper asks user to choose the room 
        # if there's monster or pete in the chosen room, helper will tell the user
        # while loop runs until user input is valid 
        while (not valid_input):    
            print(f" Helper: You made here to {currentRoom}")
            print()
            print (" Helper: You can ask me whether a monster or Pete is in a certain room.")
            print()
            room = input(f" which room do you want to check? \n Here are the lists: {display_room}: \n >")
            print()
            if room not in rooms:
                print(" please, type the valid room name")
            elif 'item' not in rooms[room]:
                print(f" Helper: I see nothing in the {room}")
                valid_input = True
            elif "Monster" in rooms[room]['item']:
                time.sleep(1)
                print(f" Helper: There is monster in {room}")
                print()
                print(" Helper left the room")
                valid_input = True
            elif "Pete" in rooms[room]['item']:
                time.sleep(1)
                print(f" Helper: Your pet is in {room}. good luck! ")
                print(" Helper left the room")
                valid_input = True
            else:
                time.sleep(1)
                print(f" Helper: I don't feel anything in {room}")
                print(" Helper left the room")
                valid_input = True
                time.sleep(1)
            
            kitchen_helper = True
        time.sleep(1)
            





