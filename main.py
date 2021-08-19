from discord.ext import commands
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path="config")
"""client = discord.Client()

@client.event
async def on_ready():
    #savoir si le bot est prêt à executer une commande
    print("Le bot est prêt.")


@client.event
async def on_message(message):
    if message.content.lower() =="test":
        await message.channel.send("ok", delete_after=5)

    #print(message.content)"""

class GitSpeak(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")


Git_speak = GitSpeak()
Git_speak.run(os.getenv("TOKEN"))