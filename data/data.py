from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Color:
    color_name: str = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
