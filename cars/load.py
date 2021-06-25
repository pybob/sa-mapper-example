import csv

from .database import Database
from .schemas import Car

CARS_DATA = "cars/cars.csv"


def _load_cars_from_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def import_cars(db, path=CARS_DATA):
    for row in _load_cars_from_csv(path):
        vin = row["vin"]
        if db.get_cars(vin=vin):
            print(f"Car with vin {vin} already in DB")
            continue
        car = Car(**row)
        db.add_car(car)
    db.commit()


if __name__ == "__main__":  # pragma: no cover
    db = Database()
    db.create_tables()
    import_cars(db)
