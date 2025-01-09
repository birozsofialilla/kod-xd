import typing
import os
import csv

from data.basic.model_dataclasses import Person, Car, Airport
from model_dataclasses import Motorbike, Street


def read_people(path: str, file_name: str = "people.csv", heading: bool = True, delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name if file_name is not None else "people.csv"), "r") as file:
        rows = csv.reader(file, heading=heading, delimiter=delimiter)
        return [Person(row[0], row[1], int(row[2]), bool(row[3])) for row in rows]


def write_people(people: list[Person], path:  str = "", file_name: str = "people.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "people.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for person in people:
            writer.writerow([person.id, person.name, person.age, person.male])


def read_motorbikes(path: str, file_name: str = "motorbikes.csv", delimiter: str = ";") -> list[Motorbike]:
    with open(os.path.join(path, file_name if file_name is not None else "motorbikes.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Motorbike(row[0], row[1], int(row[2]), bool(row[3])) for row in rows]


def write_motorbikes(motorbikes: list[Motorbike], path:  str = "", file_name: str = "motorbikes.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "motorbikes.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for motorbike in motorbikess:
            writer.writerow([motorbike.plate, motorbike.type, motorbike.year, motorbike.automatic, motorbike.owner_id])


def read_streets(path: str, file_name: str = "streets.csv", delimiter: str = ";") -> list[Street]:
    with open(os.path.join(path, file_name if file_name is not None else "streets.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Street(row[0], row[1], row[2], row[3], row[4]) for row in rows]


def write_streets(streets: list[Street], path:  str = "", file_name: str = "streets.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "streets.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for street in streets:
            writer.writerow([street.code, street.name, street.city, street.state, street.country])


def read(entity_type: typing.Type[object], path: str, file_name: str = None, delimiter: str = ";") -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Motorbike:
        return read_motorbikes(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Street:
        return read_streets(path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


def write(entities: list[object], path: str, file_name: str = None, delimiter: str = ";") -> None:
    if isinstance(entities[0], Person):
        return write_people([typing.cast(Person, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    elif isinstance(entities[0], Motorbike):
        return write_motorbikes([typing.cast(Motorbike, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    elif isinstance(entities[0], Airport):
        return write_streets([typing.cast(Street, e) for e in entities], path, file_name=file_name,
                              delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")
