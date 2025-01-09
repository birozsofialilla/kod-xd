from dataclasses import dataclass, field

@dataclass
class Person:
    id: str = field(hash=True)
    name: str = field(repr=True, compare=False)
    age: int = field(repr=True, compare=False)
    male: bool = field(default=True, repr=True, compare=False)

@dataclass
class Motorbike:
    plate: str = field(hash=True)
    type: str = field(repr=True, compare=False)
    year: int = field(repr=True, compare=False)
    automatic: bool = field(default=True, repr=True, compare=False)
    owner_id: str = field(default=None, repr=True, compare=False)  # Hivatkozás Person ID-re

@dataclass()
class Street:
    code: str = field(hash=True)
    name: str = field(repr=True, compare=False)
    city: str = field(repr=True, compare=False)
    state: str = field(repr=True, compare=False)
    country: str = field(repr=True, compare=False)
