import discord
import logging
from discord.ext import commands
from settings import BOT_NAME, BOT_AUTHOR

logger = logging.getLogger(__name__)

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        logger.info("Info cog initialized")

    @commands.command()
    async def info(self, ctx):
        logger.info(f"Info command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        info_board = discord.Embed(
            title=BOT_NAME,
            description="This bot made with the egeyardimci bot template.",
            colour=discord.Colour.red()
        )
        info_board.set_footer(text=BOT_NAME)
        info_board.set_author(name=BOT_AUTHOR)
        info_board.add_field(name="Commands", value="Type .help for commands.", inline=True)
        await ctx.send(embed=info_board)

    @commands.command()
    async def avatar(self, ctx):
        logger.info(f"Avatar command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        await ctx.send(ctx.author.display_avatar.url)

    @commands.command()
    async def help(self, ctx):
        logger.info(f"Help command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        info_board = discord.Embed(
            title=BOT_NAME,
            colour=discord.Colour.blue()
        )
        info_board.set_footer(text=BOT_NAME)
        info_board.set_author(name=BOT_AUTHOR)
        info_board.add_field(name=".avatar", value="Shows your avatar.", inline=False)
        info_board.add_field(name=".info", value="info about bot.", inline=False)
        info_board.add_field(name=".coinflip", value="CoinFlip game.", inline=False)
        info_board.add_field(name=".joke", value="Makes a joke.", inline=False)
        info_board.add_field(name=".mirror", value="Bot mirrors your sentence.", inline=False)
        info_board.add_field(name=".giveaway", value='Only who has "admin" role can use this command.', inline=False)
        info_board.add_field(name=".brakethesentence", value='Brakes the sentence.', inline=False)
        info_board.add_field(name=".lenght", value='Give you info about the sentence.', inline=False)
        info_board.add_field(name=".minecraft", value='Shows your minecraft profile.', inline=False)
        info_board.add_field(name=".writinggame", value='Game for fast writing.', inline=False)
        info_board.add_field(name=".wiki", value='Send you the wiki link of requested thing.', inline=False)
        await ctx.send(embed=info_board)

async def setup(bot):
    await bot.add_cog(Info(bot))
