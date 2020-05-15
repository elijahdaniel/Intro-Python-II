from room import Room
from player import Player
from item import Item

import textwrap

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create Items
items = {
    'flashlight': Item('flashlight', 'Used to light up dark areas')
}

# Add items to room
# room['outside'].items.append(items['flashlight'])


# Make a new player object that is currently in the 'outside' room.
user = Player('Elijah', room['outside'])

# Write a loop that:
while True:
    # * Prints the current room name
    print(f'\nCurrent Room: {user.current_room} \n')

    # * Prints the current description (the textwrap module might be useful here).
    for txt in textwrap.wrap(user.current_room.print_description()):
        print(f'{txt}\n')

    # * Waits for user input and decides what to do.
    direction = input(
        'Enter a direction (n, s, e, w), or enter q to Quit: ').lower()

    if direction in ['n', 's', 'e', 'w']:
        # set user's current room
        user.current_room = user.move_to(direction, user.current_room)
        continue

    # If the user enters "q", quit the game.
    if direction in ['q', 'exit', 'quit', 'stop', 'done']:
        break
