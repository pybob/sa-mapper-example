import csv

from .db import Database
from .schemas import Car

CARS_DATA = "cars/cars.csv"


def _load_cars_from_csv(path=CARS_DATA):
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def import_cars():
    db = Database()
    for row in _load_cars_from_csv():
        vin = row["vin"]
        if db.get_cars(vin=vin):
            print(f"Car with vin {vin} already in DB")
            continue
        car = Car(**row)
        db.add_car(car)
    db.commit()
    print(f"{db.get_number_of_cars()} cars in db")


if __name__ == "__main__":
    import_cars()
