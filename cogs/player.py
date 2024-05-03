import discord
from discord.ext import commands
from discord.ui import Button, View
from cogs.session import Session

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = None
        self.class_type = None
        self.level = 1
        self.health = 100
        self.mana = 50
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_spell = None

    def attack(self, enemy):
        # Implement your attack logic here
        pass

    def cast_spell(self, spell):
        # Implement your spell casting logic here
        pass

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)

    def level_up(self):
        self.level += 1
        self.health += 10
        self.mana += 5
        
    @commands.command()
    async def new_character(self, ctx):
        view = View()
        # fix this later
        session = Session()
        if session.player:
            session.player = None
        mage_button = Button(label="Mage", style=discord.ButtonStyle.primary)
        warrior_button = Button(label="Warrior", style=discord.ButtonStyle.primary)
        ranger_button = Button(label="Ranger", style=discord.ButtonStyle.primary)
        
        
        # Define callback functions for the buttons
        async def mage_callback(interaction):
            session.player = Mage(ctx.author.name)
            await interaction.response.send_message(f"You chose Mage!")
            
            
        async def warrior_callback(interaction):
            session.player = Warrior(ctx.author.name)
            await interaction.response.send_message(f"You chose Warrior!")

            
        async def ranger_callback(interaction):
            session.player = Ranger(ctx.author.name)
            await interaction.response.send_message(f"You chose Ranger!")
        
        # Assign the callbacks to the buttons
        mage_button.callback = mage_callback
        warrior_button.callback = warrior_callback
        ranger_button.callback = ranger_callback
        
        # Add the buttons to the view
        view.add_item(mage_button)
        view.add_item(warrior_button)
        view.add_item(ranger_button)
        
        # Send a message with the view containing the buttons
        await ctx.send("Choose your class:", view=view)
        

    @commands.command()
    async def status(self, ctx):
        #checks if a player exists in session
        session = Session()
        if not session.player:
            await ctx.send("No player found. Create a new character with the !new_character command")
            return
        # show the player stats
        player = session.player
        await ctx.send(f"Name: {player.name}\nClass: {player.player_class}\nHealth: {player.health}\nMana: {player.mana}\nLevel: {player.level}")


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 100
        self.player_class = 'Mage'

    def cast_spell(self, spell):
        # Implement the spell casting logic for the Mage class
        pass

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.player_class = 'Warrior'

    def attack(self, enemy):
        # Implement the attack logic for the Warrior class
        pass

class Ranger(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 120
        self.player_class = 'Ranger'

    def attack(self, enemy):
        # Implement the attack logic for the Ranger class
        pass

async def setup(bot):
    await bot.add_cog(Player(bot))