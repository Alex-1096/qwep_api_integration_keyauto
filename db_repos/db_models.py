from sqlalchemy import Column, Integer, String, DECIMAL, Index
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

# Модель таблицы с результирующими данными sqlalchemy

class Model(DeclarativeBase):
    ...


class PricesORM(Model):
    __tablename__ = 'Qwep_prices'
    __table_args__ = {"schema": "Imprice"}

    id = Column(Integer, primary_key=True)
    analyticCountReq = Column(Integer)
    analyticCountBuy = Column(Integer)
    article = Column(String)
    availabilityTotalByPeriodEnd = Column(Integer)
    avgprice = Column(DECIMAL(20, 2))
    brand = Column(String)
    cnt = Column(Integer)
    currency = Column(String)
    maxavailability = Column(Integer)
    maxprice = Column(DECIMAL(20, 2))
    minprice = Column(DECIMAL(20, 2))
    status = Column(String)
    vendor = Column(String)
    id_nom = Column(Integer, index=True)
    date_actual = Column(DATETIME2)
    date_upd = Column(DATETIME2, default=datetime.now(), onupdate=datetime.now)
