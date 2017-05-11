from discord.ext import commands
import discord
import re
class status:
    def __init__(self, bots):
        print("   [status.py] Initializing...", end="")
        self.bots = bots
    @commands.command(pass_context=True, aliases=['presence'])
    async def status(self,ctx):
            avatar = self.bots.user.avatar_url
            bot_status = status.RemovePrefix(str(ctx.message.content))
            em = status.embed(bot_status, ctx)
            await self.bots.send_message(ctx.message.channel, '', embed=em)
            await self.bots.change_presence(game=discord.Game(name=bot_status))

    def RemovePrefix(msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg

    def embed(status, ctx):
        em = discord.Embed(color=0xf2ddde)
        em.add_field(name='Status', value=status)
        em.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        return em
def setup(bots):
    bots.add_cog(status(bots))
