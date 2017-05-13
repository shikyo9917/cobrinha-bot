from discord.ext import commands

class TestCommands:
    def __init__(self, bot):
        print("   [test.py] Initializing...")
        self.bot = bot

    @commands.command(pass_context=True, aliases=['perms'])
    async def permissions(self, context):
        print(context.message.channel.permissions_for(context.message.author).manage_messages)
