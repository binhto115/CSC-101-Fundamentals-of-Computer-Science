# Name: Binh To
# Date: 10/14/2022
# Github: 113943258

from objects import Item


def enchantItem(spell: str, item: Item):
    """Given a spell and an item, returns a new item"""
    spell == spell.lower()
    if (spell == "open sesame"):
        if (item.power < 3):
            return Item("key", 1)
        else:
            return Item("axe", 901)
    elif (spell == "abracadabra"):
        if (item.type == "computer" or item.type == "calculator"):
            return Item("magic.py", 4000)
        elif item.power == 300 and item.type == "mochi":
            return Item("axe", 9001)
        else:
            return Item("twig", 2)
    elif (spell == "alakazam"):
        if (item.power == 1 and item.type == "pebble"):
            return Item("kitten", 1)
        else:
            return Item("Excalibur", 1)
    elif (spell == "hocus-pocus"):
        if (item.power > 32 and not item.type == "sword" and item.power < 32):
            return Item("sword", 9001)
        else:
            return Item("sword", 8999)
    else:
        return Item("wooden spoon", 1)
