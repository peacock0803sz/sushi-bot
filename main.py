import os
import asyncio

import discord

from getlive import get_live

client = discord.Client()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


async def watch(message):

    while(True):
        lives = ''.join(get_live())
        if lives != '現在放送中の番組はありません。':
            await message.channel.send(lives)
        elif lives == '現在放送中の番組はありません。':
            print('現在放送中の番組はありません。')
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
