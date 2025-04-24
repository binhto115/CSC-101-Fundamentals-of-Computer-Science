# Name: Binh To
# Date: 10/14/2022
# Github: 113943258

class Item:
    """Represents a powerful item to be used by a hero"""
    def __init__(self, type: str, power: int):
        self.type  = type
        self.power = power


class Hero:
    """Represents a hero in our story"""
    def __init__(self, name: str, skill: str, item: Item):
        self.name  = name
        self.skill = skill
        self.item  = item


class Monster:
    """Represents a terrifying monster"""
    def __init__(self, type: str, appearance: str, power: int):
        self.type       = type
        self.appearance = appearance
        self.power      = power


class World:
    """Represents the world that a story may take place in"""
    def __init__(self, setting: str, name: str, year: int):
        self.setting = setting
        self.name    = name
        self.year    = year
