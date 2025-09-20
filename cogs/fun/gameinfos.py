import discord
import logging
from discord.ext import commands
from settings import BOT_NAME

logger = logging.getLogger(__name__)

class GameInfos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info("GameInfos cog initialized")

    """
    Gets user's minecraft profile link.
    """
    @commands.command()
    async def minecraft(self, ctx, name):
        logger.info(f"Minecraft command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'} for username: {name}")
        url = f"https://namemc.com/profile/{name}.1"
        await ctx.send(f"Your Minecraft profile : {url}")

        minecraft_table = discord.Embed(
            title=BOT_NAME,
            colour=discord.Colour.gold()
        )

        p1, p2 = '{', '}'
        minecraft_table.add_field(name="Skull Code Minecraft 1.13 And Higher",
                                  value=f'/give @p minecraft:player_head{p1}SkullOwner:"{name}"{p2}', inline=False)
        minecraft_table.add_field(name="Skull Code Minecraft 1.13 And Lower",
                                  value=f'/give @p minecraft:skull 1 3 {p1}SkullOwner:"{name}"{p2}', inline=False)
        await ctx.send(embed=minecraft_table)

async def setup(bot):
    await bot.add_cog(GameInfos(bot))
