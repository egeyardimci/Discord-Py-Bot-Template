import  discord
from discord.ext import commands
TOKEN = 'Write Your Token'
BotStatus = "Example Bot"

client = commands.Bot(command_prefix= ".")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online,activity=discord.Game(BotStatus))

cogs = ["Functions.Fun.games","Functions.Fun.gameinfos","Functions.Fun.otherfuncommands","Functions.Info.info","Functions.Misc.misc","Functions.NewMember.newmember","Functions.Admin.admin"]

for i in cogs:
    client.load_extension(i)
    print("Loaded ",i)

client.run(TOKEN)