import json
import random


class Item:
    def __init__(self, name, type, rarity):
        self.name = name
        self.type = type
        self.rarity = rarity

    # Define a method to display the item's details
    def display(self):
        return f"Name: {self.name}\nType: {self.type}\nRarity: {self.rarity}"
    
    # Define a method to pull a random iteam from drop.json
    def random_item(self):
        # Load the JSON file containing the items
        with open('Monster Data\drops.json', 'r') as file:
            data = json.load(file)

        # Randomly select one item from the list
        selected_item = random.choice(data)

        # Return the selected item
        return selected_item

class Weapon(Item):
    def __init__(self, name, type, rarity, damage, damage_type):
        super().__init__(name, type, rarity)
        self.damage = damage
        self.damage_type = damage_type

class Armor(Item):
    def __init__(self, name, type, rarity, armor_class):
        super().__init__(name, type, rarity)
        self.armor_class = armor_class