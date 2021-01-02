from discord.ext import commands


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def wiki(self, ctx, msg):
        url: str = f"https://tr.wikipedia.org/wiki/{msg}"
        await ctx.send(f"Here : {url}")

    @commands.command()
    async def brokethesentence(self, ctx, sent):
        string: str = ctx.message.content[18:]
        vovels: list = ["a", "A", "e", "E", "u", "U", "o", "O", "i", "I"]
        k: int = -1
        while k < len(string) - 1:
            for i in vovels:
                if string[k] == i:
                    string = string.replace(string[k], "")
            k += 1
        await ctx.send(f"The Broken Sentence {string}")

    @commands.command()
    async def length(self, ctx, sent):
        sentence: str = ctx.message.content[7:]
        print(sentence)
        lenght: int = len(sentence)
        i = 0
        count: int = 0
        while i < lenght - 1:
            i += 1
            if sentence[i] == " ":
                count += 1
        word = count + 1
        letter = i + 1
        await ctx.send(f"World count : {word}, letter count : {letter}")

    @commands.command()
    async def howoldiam(self, ctx, year):
        now: int = 2021
        author = ctx.author
        print(author)
        try:
            b_year = int(year)
        except ValueError:
            await ctx.send("Please write your birth year.")
        try:
            if 0 < b_year < now:
                age = now - b_year
                await ctx.send("f{age} is your age")
            else:
                await ctx.send("Error.")
        except TypeError:
            await ctx.send("Please write your birth year.")


def setup(bot):
    bot.add_cog(misc(bot))
