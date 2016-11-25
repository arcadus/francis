import discord
import asyncio
import json

client = discord.Client()

class SecretHitler:
    '''An instance of a Secret Hitler game.'''
    def __init__(self):
        self.players = 0
        self.deck = None # some kind of representation of the policy deck, 11 fascist, 6 liberal

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
    if message.content.startswith('.help'):
        yield from client.send_message(message.author,
                                       '''Francis commands:
    `.help` : sends this help message in a pm
    `.secrethitler` : starts a game of Secret Hitler
    `.join` : join Secret Hitler
    ''')
    elif message.content.startswith('.secrethitler'):
        yield from client.send_message(message.channel, 'Secret Hitler game is starting, type `.join` to join!')
    elif message.content.startswith('.join'):
        yield from client.send_message(message.channel, '{} joined Secret Hitler.'.format(message.author))

client.run('token')
