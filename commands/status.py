from discord.ext import commands
import discord
import re

from .base import CommandBase
class status(CommandBase):
    def __init__(self, cobrinha):
        print("   [status.py] Initializing...")
        self.cobrinha = cobrinha
    @commands.command(pass_context=True, aliases=['presence'])
    async def status(self,ctx):
            avatar = self.cobrinha.user.avatar_url
            bot_status = self.remove_prefix(str(ctx.message.content))
            em = status.embed(bot_status, ctx)
            await self.cobrinha.send_message(ctx.message.channel, '', embed=em)
            await self.cobrinha.change_presence(game=discord.Game(name=bot_status))

    def embed(status, ctx):
        em = discord.Embed(color=0xf2ddde)
        em.add_field(name='Status', value=status)
        em.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        return em
