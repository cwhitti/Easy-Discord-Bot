import discord
from secret import TOKEN

#from classes.course import Course

def run_discord_bot():

    # set up bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client( intents=intents )

    user_cooldowns = {}

    #Show bot logged on successfully
    @client.event
    async def on_ready():

        await client.change_presence(activity=discord.Game(name="New Bot!"))
        print(f'{client.user} is now running!')

    # handle message
    #@client.event
    #async def on_message(msg):


    client.run( TOKEN )
