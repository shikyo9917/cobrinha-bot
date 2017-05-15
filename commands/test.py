from discord.ext.commands import command
import re

from .base import CommandBase
from model.bank_services import *

class TestCommands(CommandBase):
    def __init__(self, cobrinha):
        print("   [test.py] Initializing...")
        self.cobrinha = cobrinha

    @command(pass_context=True, aliases=['perms'])
    async def permissions(self, context):
        print(context.message.channel.permissions_for(context.message.author).manage_messages)
