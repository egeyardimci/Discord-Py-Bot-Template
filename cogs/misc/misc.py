from discord.ext import commands
import datetime
import logging

logger = logging.getLogger(__name__)

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        logger.info("Misc cog initialized")

    @commands.command()
    async def wiki(self, ctx: commands.Context, msg: str):
        logger.info(f"Wiki command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'} for: {msg}")
        url = f"https://en.wikipedia.org/wiki/{msg}"
        await ctx.send(f"Here : {url}")

    @commands.command(name="breakethesentence")
    async def brake_the_sentence(self, ctx: commands.Context, *, msg: str):
        logger.info(f"Break sentence command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        vowels = ["a", "A", "e", "E", "u", "U", "o", "O", "i", "I"]
        k = -1
        while k < len(msg) - 1:
            for i in vowels:
                if msg[k] == i:
                    msg = msg.replace(msg[k], "")
            k += 1
        await ctx.send(f"The Broken Sentence {msg}")

    @commands.command()
    async def length(self, ctx: commands.Context, *, msg: str):
        logger.info(f"Length command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
        length = len(msg)
        count = 0
        i = 0
        while i < length - 1:
            i += 1
            if msg[i] == " ":
                count += 1
        word = count + 1
        letter = i + 1
        await ctx.send(f"World count : {word}, letter count : {letter}")

    @commands.command(name="howoldiam")
    async def how_old_i_am(self, ctx: commands.Context, year: str):
        logger.info(f"Age calculation command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'} with year: {year}")
        now = datetime.date.today().year
        try:
            b_year = int(year)
            if 0 < b_year < now:
                age = now - b_year
                logger.debug(f"Calculated age {age} for year {b_year}")
                await ctx.send(f"{age} is your age")
            else:
                logger.warning(f"Invalid birth year provided: {b_year}")
                await ctx.send("You seem not to be born...")
        except (TypeError, ValueError) as e:
            logger.warning(f"Invalid year format provided: {year}, error: {e}")
            await ctx.send("Please write your birth year.")

async def setup(bot):
    await bot.add_cog(Misc(bot))
