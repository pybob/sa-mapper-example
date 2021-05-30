# separate orm from domain logic AKA repository pattern
# https://www.cosmicpython.com/book/chapter_02_repository.html

from sqlalchemy import (Column, Integer, MetaData,
                        String, Table)
from sqlalchemy.orm import mapper

from .data import Car

metadata = MetaData()

car = Table(
    'car',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('model', String(50)),
    Column('make', String(20)),
    Column('year', Integer),
    Column('vin', String(50)),
)
mapper(Car, car)
