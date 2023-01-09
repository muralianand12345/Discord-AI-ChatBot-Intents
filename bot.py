## Imports
# Discord Package
import discord
#Read Local Files
import os
#Dotenv packages
from dotenv import load_dotenv
#Importing function from ai.py
from ai import ai_response

#importing all discord intents
intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents = intents)
#getting guild opjects
guild = discord.Guild

#Client ready
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
    
#Message (runs everytime message is been sent)
@client.event
async def on_message(message):

    # ignores bot messages
    if message.author.bot: return

    # aichat bot channels
    channelIDsToListen = [ 1058683443199881267, 1052211037660794940, 1056236053763215410, 1058003036896768140 ]
    if message.channel.id in channelIDsToListen:
        TheMess = ai_response(message.content)
        await message.channel.send(TheMess)

# load .env
load_dotenv()
TOKEN = os.getenv('TOKEN')
#client login
client.run(TOKEN)