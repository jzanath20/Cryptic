# Import all needed libraries
import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

# Load .env file and grab data
load_dotenv()

BOT_TOKEN = os.getenv("MY_BOT_TOKEN")
GUILD_ID = os.getenv("MY_GUILD_ID")

# Create bot intents
intents = discord.Intents.default()
intents.message_content = True

# Create Logging Handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Init Bot Commands
#bot = commands.Bot(command_prefix='$', intents=intents)

# Create the client class
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await tree.sync(guild = discord.Object(id = GUILD_ID))
        print(f'Ready!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

# Create client object using client class
client = MyClient(intents=intents)

# Set up the tree
tree = app_commands.CommandTree(client)

# Add commands to tree - Slash command link https://gist.github.com/Rapptz/c4324f17a80c94776832430007ad40e6
@tree.command(guild = discord.Object(id = GUILD_ID))
async def slash(interaction: discord.Interaction, number: int, string: str):
    await interaction.response.send_message(f'{number = } {string = }', ephemeral = True)

@tree.command(guild = discord.Object(id = GUILD_ID))
@app_commands.describe(attachment = 'The File to upload')
async def upload(interaction: discord.Interaction, attachment: discord.Attachment):
    await interaction.response.send_message(f'Thanks for uploading {attachment.filename}!', ephemeral = True)

client.run(BOT_TOKEN, log_handler = handler)
