import random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def joke(self, ctx):
        select_joke = random.choice([
            "joke1",
            "joke2"
        ])
        await ctx.send(select_joke)

    @commands.command()
    async def mirror(self, ctx, *, msg):
        await ctx.send(msg)


async def setup(bot):
    await bot.add_cog(Fun(bot))
