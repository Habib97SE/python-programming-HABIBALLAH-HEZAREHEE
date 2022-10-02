from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, birth_year, gender, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.phone_number = phone_number

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def correct_birth_year(self):
        # if person is younger than 22 years old add 20 to birth year otherwise 19
        if get_age(self) < 22:

    def get_age(self):
        return datetime.date.today().year - self.birth_year
