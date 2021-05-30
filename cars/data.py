from dataclasses import dataclass


@dataclass
class Car:
    model: str
    make: str
    year: int
    vin: str
