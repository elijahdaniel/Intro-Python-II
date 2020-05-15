# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room

    def move_to(self, movement, current_location):
        # move in specified direction
        attribute = movement + '_to'

        # if current_loc has attribute, you can move in that direction
        if hasattr(current_location, attribute):
            # if it is, fetch room in specified direction
            return getattr(current_location, attribute)

        # Print an error message if the movement isn't allowed.
        print('\nYou cant go that way!!')

        return current_location
