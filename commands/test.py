from discord.ext.commands import command
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
from model.db import DB
from model import BankHistory

import re

from .base import CommandBase
from model.bank_services import *

class TestCommands(CommandBase):
    def __init__(self, cobrinha):
        print("   [test.py] Initializing...")
        self.cobrinha = cobrinha

    @command(pass_context=True, aliases=['t'])
    async def permissions(self, context):
        msg = str(self.remove_prefix(context.message.content))
        print(msg)
        print(msg.split(' '))

    @command(pass_context=True)
    async def history(self, c):

        session = DB.get_session()
        acc = session.query(Bank).filter_by(discord_id=c.message.author.id).first()

        history = acc.history
        if(len(history) <= 1):
            await self.cobrinha.send_message(c.message.channel, 'Sem historia disponivel')
            return
        dates = list(map(lambda v: v.created_at, history))
        values = list(map(lambda v: v.amount, history))


        days = mdates.HourLocator()   # every year
        months = mdates.DayLocator()  # every month
        fmt = mdates.DateFormatter('%d/%m')

        fig, ax = plt.subplots()
        ax.plot(dates, values)
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(fmt)
        ax.xaxis.set_minor_locator(days)

        ax.set_xlim(min(dates), max(dates))
        ax.set_ylim(0, max(values))

        ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        ax.grid(True)

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate()
        plt.title("History")

        plt.savefig('plot.png')
        plt.clf()

        await self.cobrinha.send_file(c.message.channel, 'plot.png')
