from sqlalchemy import Column, Integer, String, create_engine, func, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
import random, config
import pandas as pd

engine = create_engine('sqlite:///db.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(String)
    username = Column(String)
    type1 = Column(Boolean)
    type2 = Column(Boolean)
    type3 = Column(Boolean)
    type4 = Column(Boolean)
    type5 = Column(Boolean)
    type6 = Column(Boolean)
    type7 = Column(Boolean)
    type8 = Column(Boolean)
    type9 = Column(Boolean)
    type10 = Column(Boolean)

    def __repr__(self):
        return f"<User({self.id}, {self.tg_id}, {self.username}, {self.subscription_type},)>"

def dbCreate():
    Base.metadata.create_all(bind=engine)

def addUser(tg_id:str, username:str, type1:bool, type2:bool, type3:bool, type4:bool, type5:bool, type6:bool, type7:bool, type8:bool, type9:bool, type10:bool):
    user = User(tg_id=tg_id, username=username, type1=type1, type2=type2, type3=type3, type4=type4, type5=type5, type6=type6, type7=type7, type8=type8, type9=type9, type10=type10, )
    session.add(user)
    session.commit()
    return user


def rewriteUser(tg_id:str, username:str, type1:bool, type2:bool, type3:bool, type4:bool, type5:bool, type6:bool, type7:bool, type8:bool, type9:bool, type10:bool):
    user = getUserByTgID(tg_id)
    user.type1 = type1 if type1 else user.type1
    user.type2 = type1 if type1 else user.type2
    user.type3 = type1 if type1 else user.type3
    user.type4 = type1 if type1 else user.type4
    user.type5 = type1 if type1 else user.type5
    user.type6 = type1 if type1 else user.type6
    user.type7 = type1 if type1 else user.type7
    user.type8 = type1 if type1 else user.type8
    user.type9 = type1 if type1 else user.type9
    user.type10 = type1 if type1 else user.type10
    session.commit()
    return user

def getUserByID(key:int):
    user = session.query(User).get(key)
    return user

def getUserByTgID(key:str):
    user = session.query(User).filter_by(tg_id=key).first()
    return user

def getUserByUsername(key:str):
    user = session.query(User).filter_by(username=key).first()
    return user

def getUsersBySub(key:int):
    if key == 1:
        user = session.query(User).filter_by(type1=True)
    elif key == 2:
        user = session.query(User).filter_by(type2=True)
    elif key == 3:
        user = session.query(User).filter_by(type3=True)
    elif key == 4:
        user = session.query(User).filter_by(type4=True)
    elif key == 5:
        user = session.query(User).filter_by(type5=True)
    elif key == 6:
        user = session.query(User).filter_by(type6=True)
    elif key == 7:
        user = session.query(User).filter_by(type7=True)
    elif key == 8:
        user = session.query(User).filter_by(type8=True)
    elif key == 9:
        user = session.query(User).filter_by(type9=True)
    elif key == 10:
        user = session.query(User).filter_by(type10=True)
    return user

def checkUsers():
    import sqlite3
    conn = sqlite3.connect('db.db')
    query = "SELECT * FROM users"
    data_frame = pd.read_sql(query, conn)
    print(data_frame.head())

def exportDB():
    import sqlite3
    conn = sqlite3.connect('db.db')

    query = "SELECT * FROM users"
    data_frame = pd.read_sql(query, conn)
    excel_file_path = 'users.xlsx'
    data_frame.to_excel(excel_file_path, index=False)

    query = "SELECT * FROM meets"
    data_frame = pd.read_sql(query, conn)
    excel_file_path = 'meets.xlsx'
    data_frame.to_excel(excel_file_path, index=False)

    query = "SELECT * FROM codes"
    data_frame = pd.read_sql(query, conn)
    excel_file_path = 'codes.xlsx'
    data_frame.to_excel(excel_file_path, index=False)