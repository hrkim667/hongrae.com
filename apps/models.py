from sqlalchemy import Column, Integer, String
from apps.database import Base

class User(Base):
    __tablename__ = 'user'

    num = Column(Integer, primary_key=True)
    id = Column(String(10), unique=True)
    pw = Column(String, unique=True)

    def __init__(self, id=None, pw=None):
        self.id = id
        self.pw = pw

    def __repr__(self):
        return "{0}, {1}".format(self.id, self.pw)

class PMEB(Base):

    __tablename__ = 'pmeb'

    num = Column(Integer, primary_key=True)
    id = Column(String(10), unique=True)
    date = Column(String(10), unique=True)
    content = Column(String, unique=True)
    money = Column(Integer, unique=True)

    def __init__(self, id=None, date=None, content=None, money=None):
        self.id = id
        self.date = date
        self.content = content
        self.money = money

    def __repr__(self):
        return "{0}, {1}, {2}, {3}".format(self.id, self.date, self.content, self.money)

