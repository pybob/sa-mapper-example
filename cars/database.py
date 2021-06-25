import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from .models import metadata, Car

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def _create_engine(db_url=DATABASE_URL, echo=False):
    return create_engine(db_url, echo=echo)


def create_all(engine=None):
    engine = engine if engine else _create_engine()
    metadata.create_all(engine)


def create_session(engine=None):
    engine = engine if engine else _create_engine()
    return sessionmaker(bind=engine)()


class Database:

    def __init__(self, session=None):
        self.session = session if session else create_session()

    def commit(self):
        self.session.commit()

    def _query_cars(self):
        return self.session.query(Car)

    def get_cars(self, vin=None):
        query = self._query_cars()
        if vin is not None:
            return query.filter_by(vin=vin)
        return query.all()

    def get_number_of_cars(self):
        return self._query_cars().count()

    def add_car(self, car):
        self.session.add(car)


if __name__ == "__main__":
    create_all()
