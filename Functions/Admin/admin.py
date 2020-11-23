import  discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    give_list =[]
    @commands.command()
    @has_permissions(administrator=True)
    async def giveaway(self,ctx):
        members = ctx.guild.members
        for i in members:
            self.give_list.append(i)
        winner = random.choice(self.give_list)
        await ctx.send("{} {}".format("Winner : ", winner))

def setup(bot):
    bot.add_cog(admin(bot))
