import asyncio

import discord

from getlive import get_live

client = discord.Client()


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


@client.event
async def cron(message):
    if message.author == client.user:
        return

    if message.content.startswith('/watch'):
        for i in range(5):
            lives = '\n'.join(get_live())
            print(lives)
            await message.channel.send(lives)
            await asyncio.sleep(30)

client.run('NTQyNjM5MzQ3NDgxMDUxMTM2.Dzw78g.6LlhLGaMqH-aMVvoq1MkspPOd-c')
