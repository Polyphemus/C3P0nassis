import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
from pathlib import Path

# Creates an instance of a Client object from class discord.Client(*, intents, **options)
# Represents a client connection that connects to Discord. This class is used to interact with the Discord WebSocket and API)
client = commands.Bot(command_prefix = '>', intents=intents)


@client.event  # decorator that registers an event to listen to
async def on_ready():  # discord module function Called when the client is done preparing the data received from Discord. Usually after login is successful and the Client.guilds and co. are filled up
    # guild = client.get_guild(961853422292844574)
    print("ich bin online beep")

@client.event
# Called when a Message obj is created and sent. Class discord.Message
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()  # type str

    if msg.startswith('$hello'):
        await message.channel.send('Hello' + message.author.mention)
        
    if any(x in msg for x in ['!help', '$help', '?help', 'readme']):
        await message.channel.send('''Greetings! I am C-3POnassis, resident discord bot.
At the moment I mostly post gifs when I hear certain phrases, but I will eventually do some clever things.
Try me!''')

    # other commands hidden to preserve group privacy
client.run('[token hidden]')
