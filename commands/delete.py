from discord.ext import commands
import discord
import re
class delete:
    def __init__(self, bots):
        print("   [delete.py] Initializing...")
        self.bots = bots
    @commands.command(pass_context=True, aliases=['del','purge'])
    async def delete(self,ctx):
        limit = delete.RemovePrefix(ctx.message.content)
        if delete.check_isdigit(limit):
            if delete.check_ifhundred(int(limit)):
                await self.bots.purge_from(ctx.message.channel, limit=int(limit))
            else:
                await self.bots.send_message(ctx.message.channel, 'Please insert a number less than 100.')
        else:
            await self.bots.send_message(ctx.message.channel, 'Please insert a number.')
    def check_isdigit(limit):
        if limit.isdigit():
            return True
        else:
            return False
    def check_ifhundred(limit):
        if limit <= 100:
            return True
        else:
            return False
    def RemovePrefix(msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg


def setup(bots):
    bots.add_cog(delete(bots))
