import discord
from discord.ext import commands
import settings

from rich.logging import RichHandler
import logging
logging.basicConfig(level= logging.INFO ,handlers=[RichHandler()])
logger = logging.getLogger(__name__)

# You can also use discord.Intents.default() and then enable the ones you need
# Look at the discord.py documentation for more information on intents
# https://discordpy.readthedocs.io/en/stable/intents.html
intents = discord.Intents.all()

cogs: list = ["cogs.fun.games", "cogs.fun.gameinfos", "cogs.fun.otherfuncommands", "cogs.info.info",
              "cogs.misc.misc", "cogs.newmember.newmember", "cogs.admin.admin"]
client = commands.Bot(command_prefix=settings.BOT_PREFIX, help_command=None, intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BOT_STATUS))
    for cog in cogs:
        try:
            logger.info(f"Loading cog {cog}")
            await client.load_extension(cog)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            logger.error("Failed to load cog {}\n{}".format(cog, exc))
        else:
            logger.info(f"Loaded cog {cog}")
    logger.info("Bot is ready!")

client.run(settings.DISCORD_BOT_TOKEN)
