from discord.ext.commands import command
import discord
from model.bank_services import *

from .base import CommandBase
class GameCommands(CommandBase):
    def __init__(self, cobrinha):
        print("   [games.py] Initializing...")
        self.cobrinha = cobrinha
        self.bank_services = Services()
    @command(pass_context=True, aliases=['dice_roll'])
    async def dice(self,ctx):
            #AINDA CALCULAR AS CHANCES
            return
