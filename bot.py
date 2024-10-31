import discord
from discord.ext import commands

import settings

intents = discord.Intents.default()

cogs: list = ["cogs.fun.games", "cogs.fun.gameinfos", "cogs.fun.otherfuncommands", "cogs.info.info",
              "cogs.misc.misc", "cogs.newmember.newmember", "cogs.admin.admin"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            await client.load_extension(cog)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))
        else:
            print(f"Loaded cog {cog}")


client.run(settings.TOKEN)
