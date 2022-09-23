
# A dictionary for each room with item and direction to linking room

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
        'north' : 'Living Room'
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
        'item' : 'monster'
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

'''
pseudo code 



'''

