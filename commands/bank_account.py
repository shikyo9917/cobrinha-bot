from discord.ext.commands import command
from model.bank_services import *

from .base import CommandBase

class BankCommands(CommandBase):
    def __init__(self, cobrinha):
        print("   [bank_account.py] Initializing...")
        self.cobrinha = cobrinha
        self.bank_services = Services()

    @command(pass_context=True)
    async def deposito(self, context):
        id = context.message.author.id
        value = int(self.remove_prefix(context.message.content))
        self.bank_services.deposit(id,value)

    @command(pass_context=True)
    async def saldo(self,context):
        id = context.message.author.id
        value = self.bank_services.bank_statement(id)
        await self.cobrinha.send_message(context.message.channel, value)

    @command(pass_context=True)
    async def transferir(self, context):
        msg = str(self.remove_prefix(context.message.content)).split(' ')
        id = context.message.author.id
        mentions = context.message.mentions
        if(len(mentions) != 1):
            await self.cobrinha.send_message(context.message.channel, "Uso: ~transferir @<membro> valor")
            return
        beneficiary = mentions[0]
        value = int(msg[1])
        self.bank_services.bank_transfer(beneficiary.id,id,value)
