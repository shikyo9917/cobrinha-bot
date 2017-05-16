from .bank import *
from .db import *
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
        
        print(value)
        account.amount = int(value)
        session.commit()
        
     def bank_statement(self, id):
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        value = 0
        if(account != None):
            value = account.amount
        return value
    
     def bank_transfer(self, beneficiary_id, id, value):
        be_amount = 0
        acc_amount = 0
        
        session = DB.get_session()
        acc = session.query(Bank).filter_by(discord_id=id).first()
        be_acc = session.query(Bank).filter_by(discord_id=beneficiary_id).first()
        
        if(be_acc == None):
            be_acc = Bank(discord_id=beneficiary_id, amount=0)
            session.add(be_acc)
        
        be_amount = be_acc.amount
        be_amount = be_amount + value
        be_acc.amount = int(be_amount)

        acc_amount = acc.amount
        acc_amount = acc_amount - value
        acc.amount = int(acc_amount)

        session.commit()