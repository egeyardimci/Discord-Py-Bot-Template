from discord.ext import commands


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def wiki(self, ctx, msg):
        url = "https://tr.wikipedia.org/wiki/{}".format(msg)
        await ctx.send("Here : {}".format(url))

    @commands.command()
    async def brokethesentence(self, ctx, sent):
        string = ctx.message.content[18:]
        vovels = ["a", "A", "e", "E", "u", "U", "o", "O", "i", "I"]
        k = -1
        while k < len(string) - 1:
            for i in vovels:
                if string[k] == i:
                    string = string.replace(string[k], "")
            k = k + 1
        await ctx.send("{}{}".format("The Broken Sentence: ", string))

    @commands.command()
    async def length(self, ctx, sent):
        sentence = ctx.message.content[7:]
        print(sentence)
        uzunluk = len(sentence)
        i = 0
        count = 0
        while i < uzunluk - 1:
            i = i + 1
            if sentence[i] == " ":
                count += 1
        word = count + 1
        letter = i + 1
        await ctx.send("{}{}{}{}".format("Word Count : ", word, " Letter Count : ", letter))

    @commands.command()
    async def howoldiam(self, ctx, year):
        now = 2020
        author = ctx.author
        print(author)
        try:
            b_year = int(year)
        except ValueError:
            await ctx.send("Please write your birth year.")
        try:
            if b_year > 0 and b_year < now:
                yas = now - b_year
                await ctx.send("{}{}".format(yas, " is your age."))

            else:
                await ctx.send("Error.")
        except TypeError:
            await ctx.send("Please write your birth year.")


def setup(bot):
    bot.add_cog(misc(bot))
