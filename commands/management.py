""" This class is meant to be the manager of your server
    it means it will have commands to kick, mute and things like that"""

from discord.ext.commands import command
import discord
import re

from .base import CommandBase

class management(CommandBase):
    def __init__(self, cobrinha):
        print("   [Management.py] Initializing...")
        self.cobrinha = cobrinha

    @command(pass_context=True, aliases=['del','purge'])
    async def delete(self,context):
        limit = self.remove_prefix(context.message.content)
        if management.check_isdigit(limit):
            if management.check_ifhundred(int(limit)):
                await self.cobrinha.purge_from(context.message.channel, limit=int(limit))
            else:
                await self.cobrinha.send_message(context.message.channel, 'Please, '+context.message.author.mention+' insert a number less than 100.')
        else:
            await self.cobrinha.send_message(context.message.channel, 'Please insert a number.')

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
