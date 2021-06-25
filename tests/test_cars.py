from cars.load import import_cars


def test_db_initial_state(db):
    assert len(db.get_cars()) == 0


def test_add_cars_from_csv(db):
    import_cars(db)
    assert len(db.get_cars()) == 1000
    assert db.get_number_of_cars() == 1000


def test_no_car_can_be_inserted_twice(capfd, db, csv_file):
    import_cars(db)
    import_cars(db, csv_file)
    actual = capfd.readouterr()[0].split('\n')[0]
    expected = "Car with vin 5TDBK3EH5DS978631 already in DB"
    assert actual == expected
