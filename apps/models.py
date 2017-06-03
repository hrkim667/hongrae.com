from sqlalchemy import Column, Integer, String
from apps.database import Base

class PMEB(Base):

    __tablename__ = 'pmeb'

    num = Column(Integer, primary_key=True)
    date = Column(String(10))
    content = Column(String)
    money = Column(Integer)

    def __init__(self, date=None, content=None, money=None):
        self.date = date
        self.content = content
        self.money = money

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.date, self.content, self.money)

class Schedule(Base):

    __tablename__ = 'schedule'

    num = Column(Integer, primary_key=True)
    date = Column(String(10))
    content = Column(String)

    def __init__(self, date=None, content=None):
        self.date = date
        self.content = content

    def __repr__(self):
        return "{0}, {1}".format(self.date, self.content)
