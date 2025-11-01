import random
import logging
from discord.ext import commands

logger = logging.getLogger(__name__)

class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_member = None
        logger.info("Fun cog initialized")

    @commands.command()
    async def joke(self, ctx: commands.Context):
        select_joke = random.choice([
            "joke1",
            "joke2"
        ])
        logger.info(f"Joke command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        await ctx.send(select_joke)

    @commands.command()
    async def mirror(self, ctx: commands.Context, *, msg: str):
        logger.info(f"Mirror command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'} with message: {msg[:50]}{'...' if len(msg) > 50 else ''}")
        await ctx.send(msg)

async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
