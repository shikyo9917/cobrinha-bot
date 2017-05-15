from discord.ext.commands import command
from model.bank_services import *

class Bank:
    def __init__(self, cobrinha):
        print("   [bank_account.py] Initializing...")
        self.cobrinha = cobrinha
        self.bank_services = Services()

    @command(pass_context=True)
    async def deposito(self, context):
        self.bank_services.deposito(context)

    @command(pass_context=True)
    async def saldo(self,context):
        value = self.bank_services.saldo(context)
        await self.cobrinha.send_message(context.message.channel, value)
