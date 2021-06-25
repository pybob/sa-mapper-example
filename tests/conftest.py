import os

import pytest

from cars.database import Database
from cars.load import CARS_DATA

TEST_DB_URL = os.getenv('TEST_DATABASE_URL')


@pytest.fixture
def db():
    db = Database(db_url=TEST_DB_URL)
    db.create_tables()
    yield db
    db.drop_tables()


@pytest.fixture
def csv_file(tmp_path):
    path = tmp_path / 'cars.csv'
    with open(CARS_DATA) as f:
        content = "".join(f.readlines()[:2])
        with open(path, "w") as g:
            g.write(content)
    return path
