from dataclasses import dataclass


@dataclass(frozen=True)
class Manufacturer:
    name: str


@dataclass(frozen=True)
class Car:
    name: str
    manufacturer: Manufacturer
    year: int
    vin: str
