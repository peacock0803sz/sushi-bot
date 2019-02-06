import time

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


@client.event
while True:
    if get_live() == 0:
        break
    else:
        lives = '\n'.join(get_live())
        await message.channel.send(lives)

    time.sleep(300)


client.run('NTQyMjA2NDI5MTA1MzU2ODEw.DzqotA.BTDQKWLzNOYaP3ANyocyTy6QaTA')
