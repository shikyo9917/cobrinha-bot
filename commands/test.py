from discord.ext.commands import command
import re
from model import *

class TestCommands:
    def __init__(self, bot):
        print("   [test.py] Initializing...")
        self.bot = bot

    @command(pass_context=True, aliases=['perms'])
    async def permissions(self, context):
        print(context.message.channel.permissions_for(context.message.author).manage_messages)

    @command(pass_context=True)
    async def save(self, context):
        id = context.message.author.id
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        if(account == None):
            account = Bank(discord_id=id, amount=0)
            session.add(account)

        value = self.RemovePrefix(context.message.content)
        account.amount = int(value)
        session.commit()

    @command(pass_context=True)
    async def get(self, context):
        id = context.message.author.id
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        value = 0
        if(account != None):
            value = account.amount

        await self.bot.send_message(context.message.channel, value)

    def RemovePrefix(self, msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg
