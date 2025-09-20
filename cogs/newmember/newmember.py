from discord.ext import commands
import logging

logger = logging.getLogger(__name__)

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        logger.info("Welcome cog initialized")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.info(f"New member joined: {member} in guild: {member.guild.name}")
        channel = member.guild.system_channel
        if channel is not None:
            logger.info(f"Sending welcome message to {member} in {channel.name}")
            await channel.send(f"Welcome to the server {member.mention}.")
        else:
            logger.warning(f"No system channel found for guild {member.guild.name}, could not send welcome message")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
