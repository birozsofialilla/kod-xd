import json
import os
from typing import cast, Type

from data.basic.generator import generate_people
from data.basic.model_dataclasses import Person, Airport, Car
from model_dataclasses import Motorbike, Street


def write_people(people: list[Person], path: str = "",
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump(
            [person.__dict__ for person in people],
            file, indent=2 if pretty else None)


def read_people(path: str, file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        """
        return [
            Person(person["id"], person["name"],
                   person["age"], person["male"])
            for person in json.load(file)
        ]
        """

        def convert(d: dict) -> Person:
            return Person(**d)

        # return json.load(file, object_hook=lambda d: Person(convert))
        return json.load(file, object_hook=lambda d: Person(**d))


def read_motorbikes(path: str, file_name: str = "motorbikes", extension: str = ".json") -> list[Car]:
    file_name = file_name if file_name is not None else "motorbikes"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "r") as file:
        return [Motorbike(document["plate"], document["type"], int(document["year"]), bool(document["automatic"]))
                for document in json.load(file)]


def write_motorbikes(cars: list[Motorbike], path: str = "", file_name: str = "motorbikes", extension: str = ".json", pretty=True) -> None:
    file_name = file_name if file_name is not None else "motorbikes"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([motorbike.__dict__ for motorbike in motorbikes], file, indent=2 if pretty else None)


def read_streets(path: str, file_name: str = "streets", extension: str = ".json") -> list[Street]:
    file_name = file_name if file_name is not None else "streets"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "r") as file:
        return [Street(doc["name"], doc["code"], doc["city"], doc["state"], doc["country"])
                for doc in json.load(file)]


def write_streets(streets: list[Street], path: str = "", file_name: str = "streets", extension: str = ".json",
                   pretty=True) -> None:
    file_name = file_name if file_name is not None else "streets"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([street.__dict__ for street in streets], file, indent=2 if pretty else None)


def read(entity_type: Type[object], path, file_name: str = None, extension: str = None) -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, extension=extension)
    elif entity_type == Motorbike:
        return read_motorbikes(path, file_name=file_name, extension=extension)
    elif entity_type == Street:
        return read_streets(path, file_name=file_name, extension=extension)
    else:
        raise RuntimeError("Unknown type of entity")


def write(entities: list[object], path, file_name: str = None, extension: str = None, pretty=True) -> None:
    if isinstance(entities[0], Person):
        return write_people([cast(Person, e) for e in entities],
                            path, file_name=file_name,
                            extension=extension, pretty=pretty)
    elif isinstance(entities[0], Motorbike):
        return write_motorbikes([cast(Motorbike, e) for e in entities],
                          path, file_name=file_name,
                          extension=extension, pretty=pretty)
    elif isinstance(entities[0], Street):
        return write_streets([cast(Street, e) for e in entities],
                              path, file_name=file_name,
                              extension=extension, pretty=pretty)
    else:
        raise RuntimeError("Unknown type of entity")

if __name__ == "__main__":
    people = generate_people(10)
    write_people(people, "D:/", pretty=False)
    for person in read_people("D:/"):
        print(person)
