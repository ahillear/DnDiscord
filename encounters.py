import json
import random

def get_monster_by_challenge(challenge_rating):
    # Load the JSON file containing the monsters
    with open('Monster Data\srd_5e_monsters.json', 'r') as file:
        data = json.load(file)

    # Filter the monsters based on the provided challenge rating
    filtered_monsters = [monster for monster in data if monster.get('Challenge', '').startswith(str(challenge_rating))]

    # If no monsters found with the given challenge rating, return a message
    if not filtered_monsters:
        return f"No monsters found with Challenge rating {challenge_rating}."

    # Randomly select one monster from the filtered list
    selected_monster = random.choice(filtered_monsters)

    # Return the selected monster
    return selected_monster

''' Example usage:
# Assuming 'monsters.json' contains a list of monsters in the described format.
json_path = 'Monster Data\srd_5e_monsters.json'
challenge_rating = 8  # Specify the desired challenge rating

# Get a monster with the given challenge rating
monster = get_monster_by_challenge(json_path, challenge_rating)

# Print the selected monster
print(monster['name'])  # Print the name of the selected monster
'''

# Monster attack function
def monster_attack(player, monster):
    # Calculate the damage dealt by the monster
    attack = monster.get('Actions', [{}])[0].get('attack_bonus', 0)  # Get the attack bonus of the monster
    damage = random.randint(1, 10)  # Random damage between 1 and 10

    # Subtract the damage from the player's health
    player.take_damage(damage)

    # Return the damage dealt
    return damage