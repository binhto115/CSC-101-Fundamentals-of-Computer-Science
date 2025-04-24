# Name: Binh To
# Date: 10/14/2022
# Github: 113943258

import objects
import magic

# Complete the following object instantiation statements for task 1:
world = objects.World("Fantasy", "Chronica", 1992)
monster = objects.Monster("Mythic Dragon", "dark", 2500)
hero = objects.Hero("Rosemary", "traveling", objects.Item("mochi", 300))

# Change this string for task 2:
spell = "abracadabra"

# The following lines of code containing conditional statements will tell
# the story given the data initialized above.
# You should not modify any of the code below.
if world.setting == "Sci-Fi":
    print("Welcome to planet Mars in the year:", world.year)
    print("Fantasy heroes don't not exist here.")
    exit(1)
elif world.setting == "Fantasy":
    print("Once upon a time, there lived a soon to be hero named", hero.name)
else:
    print("There is no story to tell here.")
    exit(1)

if hero.skill == "farming":
    print(hero.name, "spent many years tending to their farm.")
elif hero.skill == "basketball" or hero.skill == "baseball" or hero.skill == "swimming":
    print(hero.name, "was a star athlete.")
elif hero.skill == "exploring" or hero.skill == "traveling":
    print(hero.name, "spent many years traveling across the realm of", world.name)
else:
    print(hero.name, "lived a personally enjoyable life until old age.")
    exit(1)

if (world.year > 2022):
    print(world.name, "was in chaos and few survived .")
    exit(1)
elif (not world.year == 1992):
    print("Nothing exciting happened in", world.name, "this year.")
    exit(1)
else:
    if (hero.skill == "traveling"):
        print(hero.name, "by chance came across a", hero.item.type, "one day.")
    else:
        print("However, a terrible", monster.type, "invaded", world.name, "and ruled over the land for eternity.")
        exit(1)

print("During this time, a terrible", monster.appearance, monster.type, "invaded", world.name)

print("Legend has it, a", monster.appearance, monster.type, "would be defeated by a magic sword one day.")

print(f"{hero.name} wanted to defeat the {monster.type} and sought out a legendary wizard to enchant the {hero.item.type}.")

print(f"\"Ah, you brought me a {hero.item.type}. I can enchant this with an enchantItem function call, but the result depends on the item and the spell!\" said the wizard.")

print(f"\"Use the spell \"{spell}\"\" said {hero.name}.")

hero.item = magic.enchantItem(spell, hero.item)

print(f"So the Wizard did just that and the enchantment created a(n) {hero.item.type}!")

print(f"Now with a(n) {hero.item.type}, {hero.name} confronted the {monster.appearance} {monster.type}.")

if ((hero.item.type == "sword" or hero.item.type == "axe" or hero.item.type == "hammer") and hero.item.power > 9000):
    print(f"{hero.name} defeated the {monster.type} in one swing.")
    print(f"Everyone in {world.name} lived happily ever after. The End.")
    exit(0)
elif (hero.item.type == "kitten"):
    print(f"The {monster.appearance} {monster.type} exclaimed: \"What an adorable little kitten! How could I ever bring destruction to a world with such a creature? I concede.\"")
    print(f"Everyone in {world.name}, including the {monster.type}, lived happily ever after. The End.")
    exit(0)
else:
    print(f"But {hero.name} could not defeat the {monster.type}.")
    print(f"The {monster.type} ruled {world.name} forever after.")
    exit(1)
