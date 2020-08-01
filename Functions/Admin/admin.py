import  discord
import random
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    """
    YOU SHOULD GIVE YOUR SELF A ROLE NAMED ADMIN TO USE THIS LIKE THAT OR YOU CAN EDIT THE CODE AND DO IT BY PERMISSIONS.
    """

    give_list =[]
    @commands.command(pass_context=True)
    async def giveaway(self,ctx):
        author = ctx.message.author
        role_names = [role.name for role in author.roles]
        if "Admin" in role_names:
            kisi = ctx.guild.members
            for i in kisi:
                self.give_list.append(i)
            kazanan = random.choice(self.give_list)
            await ctx.send("{} {}".format("Winner : ", kazanan))
        else:
            await ctx.send("You don't have permission!")

def setup(bot):
    bot.add_cog(admin(bot))