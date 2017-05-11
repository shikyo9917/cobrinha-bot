from discord.ext import commands
import manager
import discord
import logging

class cobrinha(commands.Bot):


    async def on_ready(self):
        print('Logged in as')
        print("Username: "+bots.user.name)
        print("ID: "+bots.user.id)
        print('==========\n')
        for extension in manager.extensions:
            print(f"  Loading {extension}...")
            bots.load_extension("commands." + extension)
            print(f"  Loading of module {extension} completed.")
        print("Extension loading complete.\n")

if __name__ == '__main__':
    bots = cobrinha(command_prefix='~')
    bots.run('MzEyMTg4MTcwMTM5ODYxMDAy.C_XbcQ.lifp9LTw7Bmu78366R_d-Hfr71c')
