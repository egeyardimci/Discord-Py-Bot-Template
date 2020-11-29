import random
from discord.ext import commands
import random

from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def joke(self, ctx):
        selectjoke = random.choice([
            "joke1",
            "joke2"
        ])
        await ctx.send(selectjoke)

    @commands.command()
    async def mirror(self, ctx, message):
        await ctx.send(message)


def setup(bot):
    bot.add_cog(fun(bot))
