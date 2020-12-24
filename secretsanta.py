import random
import discord
import asyncio
import numpy as np
from discord import DMChannel
from discord.ext import commands

TOKEN = ''

client = discord.Client()
user = discord.User
bot = commands.Bot(command_prefix='!')
print('Starting')

@bot.command()
async def santatime(ctx):
    ids = {
    'name': 'id',
    'name2': 'id2',
    'name3': 'id3'
    }

    santa = list(np.random.choice(list(ids.keys()), len(list(ids.keys())), replace = False))
    recvr = []
    for i in range(-1, len(santa)-1):
	    recvr.append(santa[i])

    for j in range(len(santa)):
        santaid = (ids[santa[j]])
        user = await bot.fetch_user(santaid)
        message = ("{}, you are {}'s secret santa! Go get them a good gift!".format(santa[j], recvr[j]))
        await DMChannel.send(user, message)
    
bot.run(TOKEN)
