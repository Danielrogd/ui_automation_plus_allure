import os
import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_Ru')
Faker.seed()


def generated_person():
    yield Person(
        full_name=f'{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name}',
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 50),
        salary=random.randint(30000, 95000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),

    )


def generated_file():
    current_dir = os.path.dirname(__file__)
    generated_file_dir = os.path.join(current_dir, 'GENERATED_FILE')
    path = os.path.join(generated_file_dir, f'filetest{random.randint(0, 999)}.txt')
    with open(path, 'w+') as file:
        file.write(f'hello world{random.randint(0, 999)}')
    return file.name, path
