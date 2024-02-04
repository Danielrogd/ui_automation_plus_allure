from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_Ru')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=f'{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name}',
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),

    )


def generated_color():
    yield Color(
        color_name=['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Indigo', 'Magenta', 'Aqua']
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:15",
    )
