from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func
from .db import DB

class Bank(DB.Base):
    __tablename__ = 'loli_bank'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    discord_id = Column(String(30), index=True)
    amount = Column(BigInteger)
