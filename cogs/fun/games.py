import os
import random
from PIL import Image, ImageDraw
from PIL import ImageFont
import discord
from discord.ext import commands

"""
Implements a basic fast writing game with images.
TODO: This implementation has a global state issue where only one game can be active at a time across all servers. 
This should be fixed by managing game state per guild/server.
"""
class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    is_game_active = 0
    sentences = ["sent1", "sent2", "sent3"]
    sentence_to_write = ""

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.is_game_active == 1:
            if self.sentence_to_write == ctx.content:
                await ctx.channel.send(f"{ctx.author} won the game !")
                self.is_game_active = 0

    @commands.command(name="writinggame")
    async def writing_game(self, ctx):
        if self.is_game_active == 0:
            self.sentence_to_write = random.choice(self.sentences)

            img = Image.new('RGB', (1600, 80), color=(73, 109, 137))
            d = ImageDraw.Draw(img)

            try:
                fnt = ImageFont.truetype('arial.ttf', 38)
            except (OSError, IOError):
                fnt = ImageFont.load_default()
                
            d.text((20, 20), "{}".format(self.sentence_to_write), font=fnt, fill=(255, 255, 0))
            img.save("pil_text_font.png")

            await ctx.send("Sentence you need to write : ")
            await ctx.send(file=discord.File("pil_text_font.png"))
            
            # Clean up the image file after sending
            # TODO: Find a better way to handle temporary files
            os.remove("pil_text_font.png")

            self.is_game_active = 1
        else:
            await ctx.send("Game is being played now!")

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send("Heads" if random.randint(1, 2) == 1 else "Tails")

async def setup(bot):
    await bot.add_cog(Games(bot))
