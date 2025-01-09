import random
from data.basic.model_dataclasses import Car, Airport, Person


def generate_people(n: int, male_ratio: float = 0.5, min_age: int = 0, max_age: int = 100) -> list[Person]:
    assert n > 0
    assert 0 < male_ratio < 1
    assert 0 <= min_age <= max_age

    people = []
    for i in range(n):
        male = random.random() < male_ratio
        name = f"Person-{i}"  # Kézzel generált név
        age = random.randint(min_age, max_age)
        people.append(Person(
            f"O-{str(i).zfill(6)}",
            name,
            age,
            male))

    return people


def generate_cars(n: int, automatic_ratio: float = 0.2, min_year: int = 1950, max_year: int = 2021) -> list[Car]:
    assert n > 0
    assert 0 < automatic_ratio < 1
    assert 1950 <= min_year
    assert min_year <= max_year <= 2021

    cars = []
    for i in range(n):
        automatic = random.random() < automatic_ratio
        plate = f"CAR-{str(i).zfill(4)}"  # Kézzel generált rendszám
        car_type = f"CarType-{random.randint(1, 5)}"  # Kézzel generált típus
        year = random.randint(min_year, max_year)
        cars.append(Car(
            plate,
            car_type,
            year,
            automatic))

    return cars


def generate_airports(n: int, country: str = None, city: str = None) -> list[Airport]:
    assert n > 0

    airports = []
    for i in range(n):
        code = f"AP-{str(i).zfill(3)}"  # Kézzel generált kód
        name = f"Airport-{i}"  # Kézzel generált név
        city_name = f"City-{i}"  # Kézzel generált város
        state = f"State-{i}"  # Kézzel generált állam
        country_name = country if country else "Country-XYZ"  # Kézzel generált ország

        airports.append(Airport(
            code,
            name,
            city_name,
            state,
            country_name))

    return airports
