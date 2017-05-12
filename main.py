from discord.ext.commands import Bot
# import manager
import discord
import logging
import sys
import inspect
import commands
import os
from read_env import read_env

class cobrinha(Bot):

    async def on_ready(self):
        print('Logged in as')
        print("Username: "+bots.user.name)
        print("ID: "+bots.user.id)
        print('==========\n')
        self.loadCommands()
        print("Extension loading complete.\n")

    def loadCommands(self):
        commandClasses = inspect.getmembers(commands, inspect.isclass)
        for command in commandClasses:
            self.add_cog(command[1](self))


if __name__ == '__main__':
    read_env()
    bots = cobrinha(command_prefix='~')
    bots.run(os.environ['TOKEN'])
