import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class DB:
    session = None
    engine = None
    Base = declarative_base()

    def get_session():
        if(DB.session != None):
            return DB.session

        engine = DB.get_engine()

        Session = sessionmaker(bind=engine)
        DB.session = Session()
        return DB.session

    def get_engine():
        if(DB.engine != None):
            return DB.engine

        DB.engine = create_engine(os.environ['DB_CONNECTION'], echo=True)
        return DB.engine

    def bootstrap():
        DB.Base.metadata.create_all(DB.get_engine())
