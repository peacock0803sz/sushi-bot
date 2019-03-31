import os
import time

import discord

from getlive import get_live

client = discord.Client()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    lives = ''.join(get_live())
    if message.author == client.user:
        return

    if message.content.startswith('/sushi now'):
        await message.channel.send(lives)

    if message.content.startswith('/sushi watch'):
        for i in range(228):
            if lives != '現在放送中の番組はありません。':
                await message.channel.send(lives)
            elif lives == '現在放送中の番組はありません。':
                print('現在放送中の番組はありません。')
            time.sleep(300)

client.run(DISCORD_TOKEN)
