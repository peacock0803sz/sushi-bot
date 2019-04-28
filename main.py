import os
import asyncio

import discord

from getlive import get_live

client = discord.Client()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']


@client.event
# async def on_ready():
#     print('I have logged in as {0.user}'.format(client))


async def watch(message):

    before_result = ''
    while(True):
        result = ''.join(get_live())
        if result != before_result:
            await message.channel.send(result)
        before_result = result
        await asyncio.sleep(300)


@client.event
async def on_message(message):

    lives = ''.join(get_live())
    if message.author == client.user:
        return

    if message.content.startswith('/sushi now'):
        await message.channel.send(lives)

    if message.content.startswith('/sushi watch'):
        client.loop.create_task(watch(message))

client.run(DISCORD_TOKEN)
