import discord
import logging
import random
from PIL import Image # use pip install Pillow
from secret import TOKEN

log_file = "logs.txt"
gen_color_path = "hex_colors/randomly_generated"
usr_color_path = "hex_colors/from_user"

img_height = 250
img_width = 250

def run_discord_bot():

    # Set up bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client( intents=intents )

    # set up log
    logging.basicConfig(level=logging.INFO, filename=log_file,filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")

    # Set prefix
    prefix = '!'

    # Show bot logged on successfully
    @client.event
    async def on_ready():

        await client.change_presence(activity=discord.Game(name="New Bot!"))
        print(f'{client.user} is now running!')

    @client.event
    async def on_join():

        logging.info(f"Joined new server - {guild.name}")

    # Message Handler
    @client.event
    async def on_message(msg):

        # Grab the Message Content
        content = msg.content

        # Grab the author's name
        name = msg.author.name

        args = msg.content.split()

        if msg.author == client.user:
            return 0 # skip messages sent by bot

        # Check if the message starts with a known command
        if content.startswith(prefix + "hello"):

            logging.info(f"{name} used command: {prefix}hello")

            # Send hello back
            await msg.channel.send(f"Hello, {name}!")

        elif content.startswith(prefix + "help"):

            embed = discord.Embed(title="Showing commands...")

            embed.add_field(name=prefix + "help", value="Help command")
            embed.add_field(name=prefix + "genhex", value="Generate a random hex color")
            embed.add_field(name=prefix + "showhex <HEX CODE>", value="View a hex color code")

            await msg.channel.send(embed=embed)
            
        elif content.startswith(prefix + "genhex"):

            hex_code = generate_random_hex_color()

            logging.info(f"{name} generated a new color: {hex_code}")

            r, g, b = hex_to_rgb(hex_code)

            image = generate_color_image((r, g, b))

            image_path = save_image( image, gen_color_path, hex_code )

            embed = discord.Embed(title="Random Color", description=hex_code,
                                    color=int(hex_code[1:], 16))

            file = discord.File(image_path, filename=f"{hex_code}.png")

            await msg.channel.send(embed=embed, file=file)

        elif content.startswith(prefix + "showhex"):

            hex_code = args[1]

            logging.info(f"{name} tried hex: {hex_code}")

            if hex_code.startswith('#'):

                hex_code = hex_code[1:]

            try:

                int(hex_code,16)

                r,g,b = hex_to_rgb(hex_code)

                image = generate_color_image((r, g, b))

                image_path = save_image( image, usr_color_path, hex_code )

                logging.info(f"VALID HEX CODE: {hex_code}")

                embed = discord.Embed(title="Showing Color", description=hex_code)

                file = discord.File(image_path, filename=f"{hex_code}.png")

                await msg.channel.send(embed=embed, file=file)

            except ValueError as e:

                logging.info(f"INVALID HEX CODE: {hex_code}")

                embed = discord.Embed(title="Sorry, that hex code is not a valid color.",
                                        description=hex_code)

                await msg.channel.send(embed=embed)

    # Run Bot with Token
        # Should be  the very last command inside of run_discord_bot
    client.run( TOKEN )

def generate_color_image(color):

    image = Image.new("RGB", (img_height, img_width), color)

    return image

def generate_random_hex_color():

    hex_chars = '0123456789ABCDEF'
    color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))

    return color

def hex_to_rgb(hex_color):
    # Remove the '#' symbol if present
    if hex_color.startswith('#'):

        hex_color = hex_color[1:]

    # Convert hex to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return r, g, b

def save_image( image, path, hex_code ):

    image_path = path + "/" + str(hex_code) + ".jpg"

    image.save(image_path)

    return image_path
