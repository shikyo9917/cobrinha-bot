from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from .base_table import BaseTable
from .db import DB

class Bank(DB.Base, BaseTable):
    __tablename__ = 'loli_bank'

    discord_id = Column(String(30), index=True)
    amount = Column(BigInteger)

    history = relationship('BankHistory', back_populates="account")
