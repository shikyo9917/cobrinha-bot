from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, func
from sqlalchemy.orm import relationship
from .base_table import BaseTable
from .db import DB

class BankHistory(DB.Base, BaseTable):
    __tablename__ = 'bank_history'

    account_id = Column(Integer, ForeignKey('loli_bank.id'))
    amount = Column(BigInteger)
    description = Column(String)

    account = relationship('Bank', back_populates="history")
