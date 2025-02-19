from sqlalchemy import Column, Integer, String, create_engine, func
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
    param1 = Column(String) #любой параметр который пристваиваем пользователю

    def __repr__(self):
        return f"<User({self.id}, {self.tg_id}, {self.username}, {self.param1},)>"

def dbCreate():
    Base.metadata.create_all(bind=engine)

def addUser(tg_id:str, username:str, param1:str):
    user = User(tg_id=tg_id, username=username, param1=param1)
    session.add(user)
    session.commit()
    return user


def rewriteUser(tg_id:str, username:str, param1:str):
    user = getUserByTgID(tg_id)
    user.param1 = param1 if param1 else user.param1
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