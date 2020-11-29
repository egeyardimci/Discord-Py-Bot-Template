from discord.ext import commands


class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome to the server {0.mention}.'.format(member))


def setup(bot):
    bot.add_cog(welcome(bot))
