import discord
from secret import TOKEN

def run_discord_bot():

    # Set up bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client( intents=intents )

    # Set prefix
    prefix = '!'

    # Show bot logged on successfully
    @client.event
    async def on_ready():

        await client.change_presence(activity=discord.Game(name="New Bot!"))
        print(f'{client.user} is now running!')

    # Message Handler
    @client.event
    async def on_message(msg):

        # Grab the Message Content
        content = msg.content

        # Check if the message starts with a known command
        if content.startswith(prefix + "hello"):

            # Grab the author's name
            author = msg.author.name

            # Send hello back
            await msg.channel.send(f"Hello, {author}!")

    # Run Bot with Token
        # Should be  the very last command inside of run_discord_bot 
    client.run( TOKEN )
