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
        self.linked_rooms[direction] = name
    
    def move(self, direction) -> "Room":
        return self.linked_rooms[direction]
    
    def unassign_character(self, character):
        """If the enemy was defeated it's no longer in this room"""
        self.character = None
    
    
class Character():
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        self.name = name
        self.hp = 10

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
    
    def weapon(self, name, damage, tipe):
        """Set the weapon the character can fight with"""
        self.weapon = {"weapon": name, "damage": damage, "type": tipe}


class Enemy(Character):
    """Enemy creature to interact with"""

    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
    
    def talk(self):
        """What will the enemy say"""
        return self.conversation
    
    def fight(self, item):
        """Did you win?"""
        return self.weakness ==item
    
    def get_defeated(self):
        global killed_enemies
        killed_enemies+=1
        return killed_enemies

    
class Friend(Character):

    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
    
    def talk(self):
        """What will the enemy say"""
        return self.conversation
    
    def treat(self, item):
        """Did you win?"""
        return self.weakness ==item

class UniqueEnemy(Enemy):
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.hp = 30
    
    def talk(self):
        """What will the enemy say"""
        return self.conversation
    
    def fight(self, item: "Item"):
        """Did you win?"""
        if item.tipe == 'weapon':
            return False
        else:
            return True

    def get_defeated(self):
        global killed_enemies
        killed_enemies+=1
        return killed_enemies


class Item:

    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        self.name = name
        self.tipe = None

    def set_description(self, description : str) -> None :
        """
        Set description for an object
        """
        self.description = description

    def describe(self) -> str :
        """"""
        return self.description
    
    def get_name(self):
        """Return the enemy description"""
        return self.name
    
class Support(Item):
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.tipe = 'support'

class Weapon(Item):
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.tipe = 'weapon'
