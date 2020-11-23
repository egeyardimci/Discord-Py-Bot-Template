import  discord
from discord.ext import commands
import settings
intents = discord.Intents.default()

cogs = ["Functions.Fun.games","Functions.Fun.gameinfos","Functions.Fun.otherfuncommands","Functions.Info.info","Functions.Misc.misc","Functions.NewMember.newmember","Functions.Admin.admin"]

client = commands.Bot(command_prefix= settings.Prefix, help_command=None, intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online,activity=discord.Game(settings.BotStatus))
    for i in cogs:
        client.load_extension(i)
        print("Loaded ",i)

client.run(settings.TOKEN)
