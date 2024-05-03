import json
import random
import player

# Monster class 
'''"name": "Goblin",
    "Armor Class": "15",
    "Hit Points": "7",
    "Resistances": "None",
    "Challenge": "1/4",
    "Actions"'''
class Monster:
    def __init__(self, name, armor, health, resistances, challenge, actions):
        self.name = name
        self.armor = armor
        self.health = health
        self.resistances = resistances
        self.challenge_rating = challenge
        self.actions = actions

    

    # Define a method to display the monster's details
    def display(self):
        return f"Name: {self.name}\nChallenge Rating: {self.challenge_rating}\nHealth: {self.health}\nAttack Bonus: {self.attack_bonus}\nDamage: {self.damage}"

    # Define a method to attack the player
    def attack(self, player):
        # Calculate the damage dealt by the monster
        damage = random.randint(1, 10)  # Random damage between 1 and 10

        # Subtract the damage from the player's health
        player.take_damage(damage)

        # Return the damage dealt
        return damage


# Define a function to get a monster by challenge rating
def get_monster_by_challenge(json_path, player):
    # Load the JSON file containing the monsters
    with open("Monster Data\test_monsters.json", 'r') as file:
        data = json.load(file)
    
    # Get the player's level   
    level = player.level

    # Filter the monsters by the specified challenge rating
    monsters = [monster for monster in data if monster['challenge_rating'] == level]

    # Randomly select one monster from the list
    selected_monster = random.choice(monsters)
    monster = Monster(selected_monster['name'], selected_monster['armor'], selected_monster['health'], selected_monster['resistances'], selected_monster['challenge_rating'], selected_monster['actions'])
    # Return the selected monster
    return monster

''' Example usage:
# Assuming 'monsters.json' contains a list of monsters in the described format.
json_path = 'Monster Data\srd_5e_monsters.json'
challenge_rating = 8  # Specify the desired challenge rating

# Get a monster with the given challenge rating
monster = get_monster_by_challenge(json_path, challenge_rating)

# Print the selected monster
print(monster['name'])  # Print the name of the selected monster
'''



async def setup(bot):
    pass