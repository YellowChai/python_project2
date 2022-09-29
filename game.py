
#!/usr/bin/env python3
# A dictionary for each room with item and direction to linking room
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
                print("Sorry, you lost")
                run = False
                
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
    
    'Hall' : {
        'south' : 'Living Room'
    },

    'Living Room' : {
        'south' : 'Library',
        'east' : 'Bathroom',
        'west' : 'Kitchen',
        'north' : 'Hall'
    },

    'Library' : {
        'south' : 'Powder Room',
        'east' : 'Study Room',
        'west' : 'Dining Room',
        'north' : 'Living Room',
        'item' : 'Helper'
    },

    'Powder Room' : {
        'south': 'Bedroom',
        'east' : 'Guest Room',
        'west' : 'Garden',
        'north': 'Library',
        'item' : 'Weapon'
    },

    'Bedroom' : {
        'east' : 'Flex Room',
        'west' : 'Music Room',
        'north': 'Powder Room',
        'item' : 'Monster'
    },

    'Bathroom' : {
        'south': 'Study Room',
        'east' : 'Living Room',
        'item' : 'Medicine' 
    },

    'Study Room' : {
        'south': 'Garden',
        'east' : 'Library',
        'north': 'Bathroom',
        'item' : 'Pet'  
    },

    'Garden' : {
        'south': 'Flex Room',
        'east' : 'Powder Room',
        'north': 'Study Room',
    },

    'Flex Room' : {
        'east' : 'Bedroom',
        'north': 'Garden',
        'item' : 'Key'  
    },

    'Kitchen' : {
        'south': 'Dining Room',
        'west' : 'Living Room',
        'item' : 'Helper'  
    },

    'Dining Room' : {
        'south': 'Guest Room',
        'west' : 'Library',
        'North': 'Kitchen',
        'item' : 'Monster'  
    },

    'Guest Room' : {
        'south': 'Music Room',
        'west' : 'Powder Room',
        'North': 'Dining Room',
    },


    'Music Room' : {
        'west' : 'Bedroom',
        'North': 'Guest Room',
        'item' : 'Secret Door'  
    },

}





currentRoom = 'Hall'

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
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        print('you are here asking')
        # if "helper" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #set the current room to the new room
        room = input("You can ask me whether a monster or your lost pet is in a certain room. which room do you want to check? ")
        if "monster" in rooms[room]['item']:
            print(f"There is monster in {room}")
        elif "pet" in rooms[room]['item']:
            print(f"Your pet is in {room}. good luck! ")
        else:
            print(f"I don't feel anything in {room}")
        time.sleep(1.5)



    ## lower case, ask only one time. 


