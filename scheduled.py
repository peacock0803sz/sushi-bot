import os
import asyncio

import discord

from getlive import get_live

client = discord.Client()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']


# @client.event
# async def on_ready():
#     print('I have logged in as {0.user}'.format(client))


async def watch(message):

    before_result = ''
    while(True):
        result = ''.join(get_live())
        if result != before_result:
            await message.channel.send(result)
        before_result = result
        await asyncio.sleep(60)


@client.event
async def on_ready():
    client.loop.create_task(watch())

client.run(DISCORD_TOKEN)
