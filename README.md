# Discord Bots, made Easy!

![](https://cdn.discordapp.com/attachments/1237634400192041015/1237665322987683882/ezgif-7-141be90d8f.gif?ex=663c7927&is=663b27a7&hm=b7cf163eb4228a372c17a941742083387189d1d6d87697f06d13c9938733e4bd&)

This repository serves as a simple, python-based template to start off any Discord Bot. It is solely a guild-based application that does NOT implement slash commands. Because slash commands are icky.

Documentation for discord.py can be found [here](https://discordpy.readthedocs.io/en/stable/)

Last updated May 8th, 2024.

## Cloning the Repo
First, clone into this repository by using the following command:

```
git clone https://github.com/cwhitti/Easy-Discord-Bot
```

Make note of where the repo was saved to so you can access it later.


## Installing Discord Module
To use this repo, you will need to install the Discord library. 

This can be done with pip. If pip is not installed, install it with [this tutorial](https://pip.pypa.io/en/stable/installation/).

Install the discord library with the following command:

```
pip install discord
```
or, for python3 users...
```
pip3 install discord
```


## Creating the Bot
You will need to register a new bot application though Discord. 

1. Head to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in.
2. At the top right, click `New Application`. This will be your bot.
3. Name your bot whatever you want and accept the terms and conditions.
4. Click the `Bot` tab on the left side of the panel.
5. **PUBLIC BOT**: On by default, this lets others add your bot with its invite-link.
6. **TOKEN**: This is your bot's personal id. Create your token and save it somewhere safe.
7. **PRIVILEDGED INTENTS**: These are permissions for your bot to communicate with Discord. Be sure to enable `PRESENCE INTENT`, `SERVER MEMBERS INTENT`, and `MESSAGE CONTENT INTENT`. Your bot will likely not work without these three intents enabled.
8. Save your changes.

That's it for the creation!

## Inviting the Bot + Permissions
Discord absolutely loves changing how to do this every three months. You need to generate an invite-link that is specific to your bot.

1. Head to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in.
2. Navigate to your new bot.

Assuming that Discord still has this under the Installation tab, use this method:

### Generating the Link
1. Click the `Installation` tab on the left side of the panel.
2. If prompted, Select `Guild Install`.
3. If `Install Link` is set to `None`, choose `Discord Provided Link` from the dropdown menu.
4. You should have a link that looks like `https://discord.com/oauth2/authorize?client_id=1234567890123456789`.
6. Be sure to set any permissions, as outlined below.
7. Save your changes.
8. Invite your bot by pasting the generated link in a Discord chat or through your browser.
9. Select the server to invite the bot to and confirm the bot's permissions.
    
### Setting Permissions
This should be in the same area as generating your invite link.
Discord loves to change how you do this, but you want to make sure your bot has both `applications.commands` and `bot` enabled.

Once `bot` has been enabled, choose the permissions you'd like for your bot. 

For a personal, small-scale bot, select `Administrator` to automatically enable all permissions. However, bots which will be used in other servers will likely need stricter permissions. It's just a security thing.

## Configuring the Token
Find your bot's token that you (hopefully) saved earlier. If you have lost your token, generate and save a new one. 

Open `secret.py` and paste your token in the file.

```
TOKEN = "YOUR.TOKEN.HERE"
```

## Running the Bot
Running the bot is easy. Ensure that you have these three files: `run.py`, `bot.py`, and `secret.py`.

- run.py: The script to run the bot.
- bot.py: The main code of the bot.
- secret.py: The "secrets" of your bot. If publishing to GitHub, I strongly recommend adding this file to .gitignore!

To run your new bot, use the following command in your console:
```
python run.py
```
or for Python3 users...
```
python3 run.py
```

The script should start and your bot should be logging in with the following message:
```
YYYY-MM-DD HR:MN:SC INFO     discord.client logging in using static token
YYYY-MM-DD HR:MN:SC INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: <SOME LONG STRING>).
```

### Using the Bot
This template comes with a build in prefix and command. The prefix for this bot is set to `!`, and the one command is `hello`.

Once you have added your bot to your server and are running it, type `!hello` into the chat. The bot will respond with `Hello, <YOUR USERNAME>`. 

## Advancing Further
Discord bots can do so much more than just send messages. They can read user input, generate images, play music, and so much more. 

I have created an example bot which shows you how to take your bot a step further. Please see [this example](https://github.com/cwhitti/Easy-Discord-Bot/tree/main/example) for more!

![](https://camo.githubusercontent.com/5a7dedcd9b84a1679a962f96acfbeb94b7e94f5a648f1ecf2d617cd43e3984ab/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f313233373931373334303730303737303335342f313233373931373336373235303731343736342f657a6769662d372d353332376466653831652e6769663f65783d36363364363365332669733d363633633132363326686d3d6633643866333639613433383838343630633961616236373135653330643134356236643331366237353937623735323330363634323739613365643137353926)

#### Thank you! - Claire
