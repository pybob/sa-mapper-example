from sqlalchemy import (Column, ForeignKey,
                        Integer, MetaData,
                        String, Table)
from sqlalchemy.orm import registry, relationship

from .car import Manufacturer, Car

mapper_registry = registry()
metadata = MetaData()

manufacturer = Table(
    'manufacturer',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

car = Table(
    'car',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('manufacturer', Integer, ForeignKey('manufacturer.id')),
    Column('year', Integer),
    Column('vin', String(50)),
)

mapper_registry.map_imperatively(Manufacturer, manufacturer)
mapper_registry.map_imperatively(Car, car, properties={
    'manufacturers': relationship(
        Manufacturer, backref='car',
        order_by=manufacturer.c.id),
})
