import os
import random
import logging
from PIL import Image, ImageDraw
from PIL import ImageFont
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

"""
Implements a basic fast writing game with images.
TODO: This implementation has a global state issue where only one game can be active at a time across all servers. 
This should be fixed by managing game state per guild/server.
"""
class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        logger.info("Games cog initialized")

    is_game_active = 0
    sentences = ["sent1", "sent2", "sent3"]
    sentence_to_write = ""

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.is_game_active == 1:
            if self.sentence_to_write == ctx.content:
                logger.info(f"Writing game won by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
                await ctx.channel.send(f"{ctx.author} won the game !")
                self.is_game_active = 0

    @commands.command(name="writinggame")
    async def writing_game(self, ctx):
        if self.is_game_active == 0:
            logger.info(f"Writing game started by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")
            self.sentence_to_write = random.choice(self.sentences)
            logger.debug(f"Selected sentence: {self.sentence_to_write}")

            img = Image.new('RGB', (1600, 80), color=(73, 109, 137))
            d = ImageDraw.Draw(img)

            try:
                fnt = ImageFont.truetype('arial.ttf', 38)
                logger.debug("Using arial.ttf font")
            except (OSError, IOError):
                fnt = ImageFont.load_default()
                logger.debug("Using default font (arial.ttf not found)")

            d.text((20, 20), "{}".format(self.sentence_to_write), font=fnt, fill=(255, 255, 0))
            img.save("pil_text_font.png")

            await ctx.send("Sentence you need to write : ")
            await ctx.send(file=discord.File("pil_text_font.png"))

            # Clean up the image file after sending
            # TODO: Find a better way to handle temporary files
            try:
                os.remove("pil_text_font.png")
                logger.debug("Temporary image file cleaned up")
            except OSError as e:
                logger.warning(f"Failed to remove temporary image file: {e}")

            self.is_game_active = 1
        else:
            logger.warning(f"Writing game attempt by {ctx.author} while game already active")
            await ctx.send("Game is being played now!")

    @commands.command()
    async def coinflip(self, ctx):
        result = "Heads" if random.randint(1, 2) == 1 else "Tails"
        logger.info(f"Coinflip command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}, result: {result}")
        await ctx.send(result)

async def setup(bot):
    await bot.add_cog(Games(bot))
