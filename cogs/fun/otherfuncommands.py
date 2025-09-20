import random
import logging
from discord.ext import commands

logger = logging.getLogger(__name__)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        logger.info("Fun cog initialized")

    @commands.command()
    async def joke(self, ctx):
        select_joke = random.choice([
            "joke1",
            "joke2"
        ])
        logger.info(f"Joke command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        await ctx.send(select_joke)

    @commands.command()
    async def mirror(self, ctx, *, msg):
        logger.info(f"Mirror command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'} with message: {msg[:50]}{'...' if len(msg) > 50 else ''}")
        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(Fun(bot))
