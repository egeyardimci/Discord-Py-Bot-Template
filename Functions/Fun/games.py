import random

import discord
from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    isgameactive = 0

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.isgameactive == 1:
            global sentencetowrite
            if sentencetowrite == ctx.content:
                await ctx.channel.send("{} won the game !".format(ctx.author))
                self.isgameactive = 0

    Sentences = ["sent1", "sent2", "sent3"]
    sentencetowrite = ""

    @commands.command()
    async def writinggame(self, ctx):
        self.isgameactive
        if self.isgameactive == 0:
            await ctx.send("Sentence you need to write : ")
            global sentencetowrite
            sentencetowrite = self.Sentences[random.randint(0, len(self.Sentences))]
            from PIL import Image, ImageDraw

            img = Image.new('RGB', (1600, 80), color=(73, 109, 137))

            d = ImageDraw.Draw(img)
            d = ImageDraw.Draw(img)
            from PIL import ImageFont
            fnt = ImageFont.truetype('arial.ttf', 38)
            d.text((20, 20), "{}".format(sentencetowrite), font=fnt, fill=(255, 255, 0))
            img.save("pil_text_font.png")

            await ctx.send(file=discord.File("pil_text_font.png"))
            self.isgameactive = 1

        else:
            await ctx.send("Game is being played now!")

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send("Heads" if random.randint(1, 2) == 1 else "Tails")


def setup(bot):
    bot.add_cog(Games(bot))
