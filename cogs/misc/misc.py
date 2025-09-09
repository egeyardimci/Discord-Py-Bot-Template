from discord.ext import commands
import datetime

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx, msg):
        url = f"https://en.wikipedia.org/wiki/{msg}"
        await ctx.send(f"Here : {url}")

    @commands.command(name="breakethesentence")
    async def brake_the_sentence(self, ctx, *, msg):
        vowels = ["a", "A", "e", "E", "u", "U", "o", "O", "i", "I"]
        k = -1
        while k < len(msg) - 1:
            for i in vowels:
                if msg[k] == i:
                    msg = msg.replace(msg[k], "")
            k += 1
        await ctx.send(f"The Broken Sentence {msg}")

    @commands.command()
    async def length(self, ctx, *, msg):
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
    async def how_old_i_am(self, ctx, year):
        now = datetime.date.today().year
        try:
            b_year = int(year)
            if 0 < b_year < now:
                age = now - b_year
                await ctx.send(f"{age} is your age")
            else:
                await ctx.send("You seem not to be born...")
        except TypeError:
            await ctx.send("Please write your birth year.")

async def setup(bot):
    await bot.add_cog(Misc(bot))
