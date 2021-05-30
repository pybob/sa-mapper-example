from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .orm import metadata, Car

DATABASE_URL = 'sqlite:///db.sqlite3'


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

    def get_cars(self):
        return self._query_cars().all()

    def get_number_of_cars(self):
        return self._query_cars().count()

    def add_car(self, car):
        self.session.add(car)


if __name__ == "__main__":
    create_all()
