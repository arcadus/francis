import discord
import asyncio

API_TOKEN = ''

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!sleep'):
        yield from asyncio.sleep(5)
        yield from client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!test'):
        yield from client.send_message(message.channel, 'hi')

client.run(API_TOKEN)
