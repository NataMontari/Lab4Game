"""
Create Your own Adventure
"""


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
        """Link room to another room"""
        self.linked_rooms[direction] = name

    def move(self, direction) -> "Room":
        """Move to another room in the set direction"""
        return self.linked_rooms[direction]


class Character():
    """A character, friendly or not, who you may see"""
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        self.name = name
        self.hit_points = 10

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

    def wield_weapon(self, name, damage, tipe):
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



class Friend(Character):
    """ A friendly character who can help you during your journey"""
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
    """A unique enemy who is defeated differently"""
    def __init__(self, name : str) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.hit_points = 30

    def talk(self):
        """What will the enemy say"""
        return self.conversation

    def fight(self, item: "Item"):
        """Did you win?"""
        if item.tipe == 'weapon':
            return False
        else:
            return True


class Item:
    """Item object"""
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
        """Describe an item"""
        return self.description

    def get_name(self):
        """Return the enemy description"""
        return self.name

class Support(Item):
    """A support item"""
    def __init__(self, name : str, heal) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.tipe = 'support'
        self.heal = heal

    def treat(self, character):
        """choose a character and treat it"""
        character.hit_points +=self.heal

class Weapon(Item):
    """Weapon item object"""
    def __init__(self, name : str, damage) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.tipe = 'weapon'
        self.damage = damage

    def attack(self, character):
        """choose a character and treat it"""
        character.hit_points -=self.damage

class Chest(Item):
    """A special item - chest, containing lots of other different items"""
    def __init__(self, name : str, locked, items) -> None :
        """
        initialize a room object, name
        """
        super().__init__(name)
        self.tipe = 'weapon'
        self.locked = locked
        self.hit_points = 5
        self.items = items

    def open(self):
        """Try to open the chest"""
        if not self.locked:
            return "Sadly, the chest is locked, but you may try to break it"
        else:
            return self.items

    def break_chest(self, weapon):
        """Try to break the chest open"""
        if weapon.damage >=self.hit_points:
            return self.items
        else:
            return "Sadly, this weapon won't work, try a different one"
