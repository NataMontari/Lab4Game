"""
Create Your own Adventure
"""
killed_enemies = 0

class Room():
    """Class Point to create a point"""
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        self.name = name
        self.linked_rooms = {"north" : None, "south": None,
                             "west": None, "east": None}

    def set_description(self, description : str) -> None :
        """
        Set description for an object
        """
        self.description = description

    def set_character(self, character : "Enemy") -> None :
        """
        Set character for a room
        """
        self.character = character

    def set_item(self, item : "Item") -> None :
        """
        Set item for this room
        """
        self.item = item

    def get_details(self) -> None :
        """
        Set description for an object
        """
        return self.description

    def get_character(self) -> "Enemy":
        """
        Set character for a room
        """
        return self.character

    def get_item(self) -> "Item" :
        """
        Set item for this room
        """
        return self.item

    def link_room(self, name, direction):
        """Link a room to a direction"""
        self.linked_rooms[direction] = name

    def move(self, direction) -> "Room":
        """move to another room"""
        return self.linked_rooms[direction]

class Enemy:
    """Enemy creature to interact with"""


    def __init__(self, name : str, description) -> None :
        """
        initialize a room object, name
        """
        self.name = name
        self.description = description

    def set_description(self, description : str) -> None :
        """
        Set description for an object
        """
        self.description = description

    def set_conversation(self, conversation : str) -> None :
        """
        Set description for an object
        """
        self.conversation = conversation

    def set_weakness(self, weakness : "Item") -> None :
        """
        Set description for an object
        """
        self.weakness = weakness

    def describe(self) -> str :
        """Return the enemy description"""
        return self.description

    def talk(self):
        """What will the enemy say"""
        return self.conversation

    def fight(self, item):
        """Did you win?"""
        return self.weakness ==item

    def get_defeated(self):
        """Check if you've defeated all necessary enemies"""
        global killed_enemies
        killed_enemies+=1
        return killed_enemies




class Item:
    """An item object"""
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        self.name = name

    def set_description(self, description : str) -> None :
        """
        Set description for an object
        """
        self.description = description

    def describe(self) -> str :
        """ Describe the item"""
        return self.description

    def get_name(self):
        """Return the enemy description"""
        return self.name
