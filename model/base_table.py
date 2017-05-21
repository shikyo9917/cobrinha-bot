from sqlalchemy import Column, Integer, DateTime, func

class BaseTable:

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
