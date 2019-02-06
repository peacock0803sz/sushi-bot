import discord

from getlive import get_live

client = discord.Client()


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('/dna'):
        lives = '\n'.join(get_live())
        await message.channel.send(lives)

client.run('NTQyMjA2NDI5MTA1MzU2ODEw.DzvYhg.Xuqb5gCBrN9hb5znTMUS0qI725A')
