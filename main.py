import asyncio

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

    if message.content.startswith('/sushi now'):
        lives = ''.join(get_live())
        await message.channel.send(lives)

    if message.content.startswith('/sushi watch'):
        lives = ''.join(get_live())
        for i in range(228):
            if lives != '現在放送中の番組はありません。':
                await message.channel.send(lives)
            elif lives == '現在放送中の番組はありません。':
                print("現在放送中の番組はありません。")
            await asyncio.sleep(300)

# TestBot: NTQyNjM5MzQ3NDgxMDUxMTM2.Dzw78g.6LlhLGaMqH-aMVvoq1MkspPOd-c
# Sushi Bot: NTQyMjA2NDI5MTA1MzU2ODEw.DzqotA.BTDQKWLzNOYaP3ANyocyTy6QaTA
client.run('NTQyMjA2NDI5MTA1MzU2ODEw.DzqotA.BTDQKWLzNOYaP3ANyocyTy6QaTA')
