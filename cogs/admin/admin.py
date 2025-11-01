import random
import logging
from discord.ext import commands

logger = logging.getLogger(__name__)

class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        logger.info("Admin cog initialized")

    """
    Picks a random user from the server to win your giveaway.
    """
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def giveaway(self, ctx: commands.Context):
        logger.info(f"Giveaway command used by {ctx.author} in {ctx.guild.name}")
        winner = random.choice(ctx.guild.members)
        logger.info(f"Giveaway winner selected: {winner}")
        await ctx.send(f"Winner: {winner.mention}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
