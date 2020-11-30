from TwitchApiPy import TwitchApiPy
from discord.ext import commands
import settings
from TwitchApiPy import TwitchApiPy
from discord.ext import commands

import settings


# This Cog is not being use for now due to an issue

class Twitch(commands.Cog, TwitchApiPy):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    api = TwitchApiPy()
    api.ClientID = settings.ClientID
    api.OAuth = settings.OAuth

    @commands.command(pass_context=True)
    async def TwitchFollower(self, ctx, name):
        Count = self.api.GetFollowerCount(name)
        await ctx.send("{}{} : {}".format("Follower count of ", name, Count))

    @commands.command(pass_context=True)
    async def TwitchChannelInfo(self, ctx, name):
        info = self.api.GetChannelInfo(name)
        info2 = self.api.GetChannelStatus(name)
        text = (
            "Channel name : {} , Last Played Game : {} , Last Streams Title : {} , Is Live : {} , Language : {}").format(
            info["name"], info["game"], info["title"], info2["islive"], info2["language"])
        await ctx.send(text)


def setup(bot):
    bot.add_cog(Twitch(bot))
