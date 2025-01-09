import random

from data.basic.model_dataclasses import Person, Motorbike, Street
from faker import Faker

from model_dataclasses import Street

fake = Faker()
def generate_people(n: int, male_ratio: float = 0.5, min_age: int = 0, max_age: int = 100) -> list[Person]:
    assert n > 0
    assert 0 < male_ratio < 1
    assert 0 <= min_age <= max_age

    people = []
    for i in range(n):

        male = random.random() < male_ratio
        name = fake.name()
        age = random.randint(min_age, max_age)
        people.append(Person(
            str(i),
            name,
            age,
            male))

    return people


def generate_motorbikes(n: int, automatic_ratio: float = 0.2, min_year: int = 1950, max_year: int = 2021) -> list[Motorbike]:
    assert n > 0
    assert 0 < automatic_ratio < 1
    assert 1950 <= min_year
    assert min_year <= max_year <= 2021

    motorbikes = []
    for i in range(n):
        automatic = random.random() < automatic_ratio
        plate = fake.license_plate()
        motorbike_type = f"MotorbikeType-{random.randint(1, 5)}"
        year = random.randint(min_year, max_year)
        motorbikes.append(Motorbike(
            plate,
            motorbike_type,
            year,
            automatic,
            str(i)))

    return motorbikes


def generate_streets(n: int, country: str = None, city: str = None) -> list[Street]:
    assert n > 0

    streets = []
    for i in range(n):
        code = f"AP-{str(i).zfill(3)}"
        name = fake.name_nonbinary() + " Street"
        city_name = fake.city()
        state = fake.state()
        country_name = fake.country()

        streets.append(Street(
            code,
            name,
            city_name,
            state,
            country_name))

    return streets
