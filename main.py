from discord.ext.commands import Bot
from read_env import read_env
import os
import inspect

import commands
from model import *

class cobrinha(Bot):

    async def on_ready(self):
        print('Logged in as')
        print("Username: "+cobrinha.user.name)
        print("ID: "+cobrinha.user.id)
        print('==========\n')
        self.loadCommands()
        print("Extension loading complete.\n")

    def loadCommands(self):
        commandClasses = inspect.getmembers(commands, inspect.isclass)
        for command in commandClasses:
            self.add_cog(command[1](self))


if __name__ == '__main__':
    read_env()
    cobrinha = cobrinha(command_prefix='~')
    # Cria as tabelas no banco caso não existam
    DB.bootstrap()

    cobrinha.run(os.environ['TOKEN'])
