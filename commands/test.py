from discord.ext.commands import command
import re

from .base import CommandBase
from model.bank_services import *

class TestCommands(CommandBase):
    def __init__(self, cobrinha):
        print("   [test.py] Initializing...")
        self.cobrinha = cobrinha

    @command(pass_context=True, aliases=['t'])
    async def permissions(self, context):
        msg = str(self.remove_prefix(context.message.content))
        print(msg)
        print(msg.split(' '))