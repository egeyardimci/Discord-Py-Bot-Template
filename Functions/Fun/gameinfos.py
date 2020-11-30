import discord
from discord.ext import commands


class GameI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def minecraft(self, ctx, name):
        url = "https://tr.namemc.com/profile/{}.1".format(name)
        await ctx.send(f"Your Minecraft profile : {url}")
        minecraft_table = discord.Embed(
            title="BotName",
            colour=discord.Colour.gold()
        )
        minecraft_table.add_field(name="Skull Code Minecraft 1.13 And Higher",
                                  value='/give @p minecraft:player_head{p1}SkullOwner:"{name}"{p2}'.format(p1="{",
                                                                                                           name=name,
                                                                                                           p2="}"),
                                  inline=False)
        minecraft_table.add_field(name="Skull Code Minecraft 1.13 And Lower",
                                  value='/give @p minecraft:skull 1 3 {p1}SkullOwner:"{name}"{p2}'.format(p1="{",
                                                                                                          name=name,
                                                                                                          p2="}"),
                                  inline=False)
        await ctx.send(embed=minecraft_table)


def setup(bot):
    bot.add_cog(GameI(bot))
