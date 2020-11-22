import  discord
import random
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def joke(self,ctx):
        jokes = ["joke1", "joke2"]
        selectjoke = random.choice(jokes)
        await ctx.send(selectjoke)

    @commands.command()
    async def mirror(self,ctx, message):
        await ctx.send(message)

def setup(bot):
    bot.add_cog(fun(bot))
