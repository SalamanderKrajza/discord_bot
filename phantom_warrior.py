import discord
import os
from auth import TOKEN 


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content in ['ok', 'OK']:
        await message.channel.send(':jagapizza: jagapizza ":ok:')

    if message.content == "$get_messages":
        counter = 0
        async for some_message in message.channel.history(limit=200):
            counter += 1
            print(f"\n\nid - {some_message.id}")
            print(f"content - {some_message.content}")
            print(f"reactions - {some_message.reactions}")


client.run(TOKEN)