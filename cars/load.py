import csv

from .db import Database
from .schemas import Car


def main():
    db = Database()
    with open("cars/cars.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            car = Car(**row)
            db.add_car(car)
    db.commit()
    print(f"{db.get_number_of_cars()} cars in db")


if __name__ == "__main__":
    main()
