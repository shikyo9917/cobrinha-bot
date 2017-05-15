from discord.ext.commands import command
import re
from model.bank_services import *

class TestCommands:
    def __init__(self, cobrinha):
        print("   [test.py] Initializing...")
        self.cobrinha = cobrinha

    @command(pass_context=True, aliases=['perms'])
    async def permissions(self, context):
        print(context.message.channel.permissions_for(context.message.author).manage_messages)

    def RemovePrefix(self, msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg
