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

    if 'here she comes' in msg:
        await message.channel.send(file=discord.File('shecomes.jpg'))

    if any(x in msg for x in ['!help', '$help', '?help', 'readme']):
        await message.channel.send('''Greetings! I am C-3POnassis, resident discord bot.
At the moment I mostly post gifs when I hear certain phrases, but I will eventually do some clever things.
Try me!''')

    if 'i see you' in msg:
        await message.channel.send(file=discord.File('see-you.gif'))

    if 'thundercats' in msg:
        await message.channel.send(file=discord.File('thundercats.gif'))

    if 'claws' in msg or 'pinch' in msg:
        await message.channel.send(file=discord.File('claws.gif'))

    if 'tits' in msg:
        await message.channel.send(file=discord.File('tits.gif'))

    if 'hoof' in msg:
        await message.channel.send(file=discord.File('hoof.gif'))

    if msg.startswith('oof') or ' oof' in msg:
        await message.channel.send(file=discord.File('targus.gif'))

    if any(x in msg for x in ['poop', 'badgas', 'fart', 'durchfall', 'sniff', 'stink']):
        print('found')
        if message.author.id == 174712203461525504:
            await message.channel.send('Oh wubang3r, you and your poop talk!')
        else:
            await message.channel.send("<@174712203461525504> get in here, we're talking poop!")

        if 'www.reddit.com' in msg:
            await message.channel.send(f'New reddit format sucks, try this link instead:\nhttps://old' + msg[msg.find('www')+3:])

client.run('[token hidden]')
