from .bank import *
from .db import *
import re
class Services:
     def RemovePrefix(msg):
        msg = re.sub(r'~[a-zA-Z0-9]+?\s','', msg)
        return msg

     def deposito(self,id,value):
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        if(account == None):
            account = Bank(discord_id=id, amount=0)
            session.add(account)
        
        print(value)
        account.amount = int(value)
        session.commit()
        
     def saldo(self, id):
        session = DB.get_session()
        account = session.query(Bank).filter_by(discord_id=id).first()
        value = 0
        if(account != None):
            value = account.amount
        return value
