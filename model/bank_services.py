from .bank import *
from .db import *
from .bank_history import BankHistory
import re

class Services:
    def RemovePrefix(msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg

    def deposit(self,id,value):
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        if(account == None):
            account = Bank(discord_id=id, amount=0)
            session.add(account)

        account.amount = int(value)
        self.create_history(account, 'deposit')
        session.commit()

    def bank_statement(self, id):
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        value = 0
        if(account != None):
            value = account.amount
        return value

    def bank_transfer(self, beneficiary_id, id, value):

        session = DB.get_session()
        acc = session.query(Bank).filter_by(discord_id=id).first()
        be_acc = session.query(Bank).filter_by(discord_id=beneficiary_id).first()

        if(be_acc == None):
            be_acc = Bank(discord_id=beneficiary_id, amount=0)
            session.add(be_acc)

        be_acc.amount += value
        acc.amount -= value

        self.create_history(be_acc, 'transfer('+acc.discord_id+')')
        self.create_history(acc, 'transfer('+be_acc.discord_id+')')

        session.commit()

    def create_history(self, account, description):
        account.history.append(BankHistory(amount=account.amount, description=description))
