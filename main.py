import discord
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path="config")
client = discord.Client()

@client.event
async def on_ready():
    #savoir si le bot est prêt à executer une commande
    print("Le bot est prêt.")


@client.event
async def on_message(message):
    if message.content.lower() =="test":
        await message.channel.send("ok", delete_after=5)

    #print(message.content)


client.run(os.getenv("TOKEN"))