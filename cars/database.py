import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from .models import metadata, Car

load_dotenv()

DEFAULT_DATABASE_URL = os.getenv("DATABASE_URL")


class Database:

    def __init__(self, db_url=None, show_sql=False):
        self.db_url = db_url or DEFAULT_DATABASE_URL
        self.show_sql = show_sql
        self._engine = self._create_engine()
        self.session = self._create_session()

    def _create_engine(self):
        return create_engine(self.db_url, echo=self.show_sql)

    def _create_session(self):
        return sessionmaker(bind=self._engine)()

    def create_tables(self):
        metadata.create_all(bind=self._engine)

    def drop_tables(self):
        metadata.drop_all(bind=self._engine)

    def commit(self):
        self.session.commit()

    def _query_cars(self):
        return self.session.query(Car)

    def get_cars(self, vin=None):
        query = self._query_cars()
        if vin is not None:
            query = query.filter_by(vin=vin)
        return query.all()

    def get_number_of_cars(self):
        return self._query_cars().count()

    def add_car(self, car):
        self.session.add(car)
