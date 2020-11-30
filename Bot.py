import discord
from discord.ext import commands

import settings

intents = discord.Intents.default()

cogs: list = ["Functions.Fun.games", "Functions.Fun.gameinfos", "Functions.Fun.otherfuncommands", "Functions.Info.info",
        "Functions.Misc.misc", "Functions.NewMember.newmember", "Functions.Admin.admin"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            client.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))


client.run(settings.TOKEN)
