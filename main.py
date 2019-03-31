import os
# import asyncio

import discord

from getlive import get_live

client = discord.Client()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('/sushi now'):
        lives = ''.join(get_live())
        await message.channel.send(lives)

client.run(DISCORD_TOKEN)
