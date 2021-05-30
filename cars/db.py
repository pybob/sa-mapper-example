from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import metadata

ENGINE = create_engine('sqlite:///db.sqlite3', echo=True)


def create_all(engine=ENGINE):
    metadata.create_all(engine)



def create_session(engine=ENGINE):
    return sessionmaker(bind=engine)()


if __name__ == "__main__":
    create_all()
