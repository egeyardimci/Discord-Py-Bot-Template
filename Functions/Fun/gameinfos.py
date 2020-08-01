import  discord
import random
from discord.ext import commands

class GameI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(pass_context=True)
    async def minecraft(self,ctx, name):
        url = "https://tr.namemc.com/profile/{}.1".format(name)
        await ctx.send("{}{}".format("Your Minecraft Profile : ", url))
        minecraft_table = discord.Embed(
            title="BotName",
            colour=discord.Colour.gold()
        )
        minecraft_table.add_field(name="Skull Code Minecraft 1.13 And Higher",value='/give @p minecraft:player_head{p1}SkullOwner:"{name}"{p2}'.format(p1="{", name=name,p2="}"),inline=False)
        minecraft_table.add_field(name="Skull Code Minecraft 1.13 And Lower",value='/give @p minecraft:skull 1 3 {p1}SkullOwner:"{name}"{p2}'.format(p1="{", name=name,p2="}"),inline=False)
        await ctx.send(embed=minecraft_table)



    """
    This part of the code was writen very badly and on my own language but it still works so i added it you can delete it if you want.
    """


    @commands.command(pass_context = True)
    async def r6(self,ctx,platform,ad):
        try:
            from urllib.request import build_opener
            from urllib.request import quote
            import re
            from bs4 import BeautifulSoup

            opener = build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]

            resource = opener.open("https://r6.tracker.network/profile/{}/{}".format(platform, ad))
            data = resource.read()
            resource.close()
            soup = BeautifulSoup(data, 'html.parser')
            kda = soup.find('div', attrs={'data-stat': 'PVPKDRatio'})
            rank = ((soup.find('div', attrs={'style': 'flex-grow: 1; display: flex; justify-content: space-between; align-items: center;'})))
            lvl = soup.find('div', attrs={'class': 'trn-defstat__value'})
            kda_csl = soup.find('div', attrs={'data-stat': 'CasualKDRatio'})
            kda_rank = soup.find('div', attrs={'data-stat': 'RankedKDRatio'})
            rank_point = soup.find('div', attrs={'class': 'trn-text--dimmed'})

            kda_dzn = re.sub("[^\w]", " ", str(kda)).split()
            rank_dzn = re.sub("[^\w]", " ", str(rank)).split()
            lvl_dzn = re.sub("[^\w]", " ", str(lvl)).split()
            kda_csl_dzn = re.sub("[^\w]", " ", str(kda_csl)).split()
            kda_rank_dzn = re.sub("[^\w]", " ", str(kda_rank)).split()
            rank_point_dzn = re.sub("[^\w]", " ", str(rank_point)).split()
            try:
                print(rank_dzn[16], rank_dzn[17])
            except:
                print("Rank=Null")

            r6_tablo = discord.Embed(
                title="{} R6 Stats".format(ad),
                colour=discord.Colour.green()
            )
            try:
                print(":::",rank_point_dzn[9],rank_point_dzn[10])
                r6_tablo.add_field(name="Platform",value="{}".format(platform).capitalize(),inline=True)
                r6_tablo.add_field(name="Total K/D",value="K/D : {}.{}".format(kda_dzn[7],kda_dzn[8]),inline=True)
                r6_tablo.add_field(name="Ranked K/D",value="K/D : {}.{}".format(kda_rank_dzn[7],kda_rank_dzn[8]),inline=True)
                r6_tablo.add_field(name="Casual K/D",value="K/D : {}.{}".format(kda_csl_dzn[7],kda_csl_dzn[8]),inline=True)
                r6_tablo.add_field(name="Level",value="Level : {}".format(lvl_dzn[4]),inline=True)
                r6_tablo.add_field(name="Rank",value="Rank : {} {}".format(rank_dzn[16],rank_dzn[17]),inline=True)

            except:
                r6_tablo.add_field(name="Rank",value="Rank : Null",inline=False)

            await ctx.send(embed=r6_tablo)
        except:
            await ctx.send("Could not find player!")

def setup(bot):
    bot.add_cog(GameI(bot))
