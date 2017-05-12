from discord.ext.commands import Bot
# import manager
import discord
import logging
import sys
import inspect
import commands

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
    bots = cobrinha(command_prefix='~')
    bots.run('MzEyMTg4MTcwMTM5ODYxMDAy.C_XbcQ.lifp9LTw7Bmu78366R_d-Hfr71c')
