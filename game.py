
#!/usr/bin/env python3
# A dictionary for each room with item and direction to linking room
from pickle import FALSE
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
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    # if the item is helper, print the option to ask quesiton. 
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print('Your current options are...')
        if rooms[currentRoom]['item'] == "Helper":
            print('ask ' + rooms[currentRoom]['item'])
            showOption(currentRoom)
        elif rooms[currentRoom]['item'] == "Monster":
            print("There is monster in this room! It's attacking you!! ")
            if "Medicine" in inventory:
                print("Thank God, you have medicine. You are healed from the attack")
                inventory.pop("Medicine")   
                showOption(currentRoom)     
            elif "Weapon" in inventory:
                print("You got rid of the monster with the weapon!")
                inventory.pop("Weapon")
                showOption(currentRoom)
            else:
                time.sleep(1)
                print("Sorry, you lost the game")
                run = False
        elif rooms[currentRoom]['item'] == "Pete":
            print("You found PETE!! He will go with you from now on")
            inventory.append("Pete")
            showOption(currentRoom)
        
        elif rooms[currentRoom]['item'] == "Secret Door" :
            print("You found the Secret Door!")
            print(f"Here's your inventory : {inventory}")
            answer = input("Do you want to leave the house now? 1.Yes 2. No" )
            if answer.lower == "1" or "yes":
                if "Key" and "Pete" in inventory:
                    print("You saved PETE!! YAY!")
                    run = False
                elif "Pete" in inventory: 
                    print("oh no, you don't have a key to open the door. Please, find the key!")
                elif "Key" in inventory:
                    print("You got out of the Monster's house, but your friend, Pete, is still waiting for you.. You lost the game")
            elif answer.lower == "2" or "no":
                print("Okay, now you know the secret door is in Music room. Let's keep on journey")
                showOption(currentRoom)
        else:
            print('get ' + rooms[currentRoom]['item'])
            showOption(currentRoom)
        
    else: 
        print('There is no item found in ' + currentRoom)
        showOption(currentRoom)
    return run 

def showOption(currentRoom):
    # print the options that player can go from current room.
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

    print("---------------------------")
    


inventory = []


rooms = {
    
    'hall' : {
        'south' : 'living Room'
    },

    'living Room' : {
        'south' : 'library',
        'east' : 'bathroom',
        'west' : 'kitchen',
        'north' : 'hall'
    },

    'library' : {
        'south' : 'powder room',
        'east' : 'study room',
        'west' : 'dining room',
        'north' : 'living Room',
        'item' : 'Helper'
    },

    'powder Room' : {
        'south': 'bedroom',
        'east' : 'guest Room',
        'west' : 'garden',
        'north': 'library',
        'item' : 'weapon'
    },

    'bedroom' : {
        'east' : 'flex Room',
        'west' : 'music Room',
        'north': 'powder Room',
        'item' : 'Monster'
    },

    'bathroom' : {
        'south': 'study Room',
        'east' : 'living Room',
        'item' : 'Medicine' 
    },

    'study Room' : {
        'south': 'garden',
        'east' : 'library',
        'north': 'bathroom',
        'item' : 'Pete'  
    },

    'garden' : {
        'south': 'flex Room',
        'east' : 'powder Room',
        'north': 'study Room',
    },

    'flex Room' : {
        'east' : 'bedroom',
        'north': 'garden',
        'item' : 'Key'  
    },

    'kitchen' : {
        'south': 'dining Room',
        'west' : 'living Room',
        'item' : 'Helper'  
    },

    'dining Room' : {
        'south': 'guest Room',
        'west' : 'library',
        'North': 'kitchen',
        'item' : 'Monster'  
    },

    'guest Room' : {
        'south': 'music Room',
        'west' : 'powder Room',
        'North': 'dining Room',
    },


    'music room' : {
        'west' : 'bedroom',
        'North': 'guest Room',
        'item' : 'secret Door'  
    },

}





currentRoom = 'hall'
kitchen_helper = 0

showInstructions()

run = True
# breaking this while loop means the game is over
while run:
    run = showStatus()
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while run and move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
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

    #if they type 'ask' first    
    if move[0] == 'ask':
        valid_input = False
        kitchen_helper = False
        library_helper = False


        if currentRoom == 'kitchen' :
            if kitchen_helper == True:
                print("Helper is not in this room anymore")
            else:
                kitchen_helper = True 
        if currentRoom == 'library' :
            if library_helper == True:
                print("Helper is not in this rrom anymore")
            else:
                library_helper = True

        display_room = []
        for i in rooms:
            if rooms[i] != currentRoom:
                display_room.append(i)

            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            
            # if "helper" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #set the current room to the new room
        print(f"Helper: You made here to {currentRoom}")
        while (not valid_input):
            room = input(f"Helper: You can ask me whether a monster or Pete is in a certain room.\n which room do you want to check? \n Here are the lists: {display_room}: \n")
            if room not in rooms:
                print("please, type the valid room name")
            elif "Monster" in rooms[room]['item']:
                time.sleep(1)
                print(f"Helper: There is monster in {room}")
                print("Helper left the room")
                valid_input = True
            elif "Pete" in rooms[room]['item']:
                time.sleep(1)
                print(f"Helper: Your pet is in {room}. good luck! ")
                print("Helper left the room")
                valid_input = True
            else:
                time.sleep(1)
                print(f"Helper: I don't feel anything in {room}")
                print("Helper left the room")
                valid_input = True
                time.sleep(1)

            kitchen_helper = True
            



    ## lower case, ask only one time. 


