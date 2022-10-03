from cgi import test
import sys
import os
import unittest


class Person:
    def __init__(self, first_name, last_name, age, personal_number) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.personal_number = personal_number

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} is {self.age} years old and has the personal number {self.personal_number}"

    def __repr__(self) -> str:
        return f"Person({self.first_name}, {self.last_name}, {self.age}, {self.personal_number})"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("First name must be a string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Last name must be a string")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        self._age = value

    @property
    def personal_number(self):
        return self._personal_number

    @personal_number.setter
    def personal_number(self, value):
        if not isinstance(value, int):
            raise TypeError("Personal number must be an integer")
        self._personal_number = value

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, age, personal_number, student_id) -> None:
        super().__init__(first_name, last_name, age, personal_number)
        self.student_id = student_id

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} is {self.age} years old and has the personal number {self.personal_number} and the student id {self.student_id}"

    def __repr__(self) -> str:
        return f"Student({self.first_name}, {self.last_name}, {self.age}, {self.personal_number}, {self.student_id})"

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, int):
            raise TypeError("Student id must be an integer")
        self._student_id = value

    def get_email_address(self):
        return f"{self.first_name}.{self.last_name}@student.example.com"


def main():
    unittest.TestCase().assertEqual((1, 2), (1, 3))


if __name__ == "__main__":
    main()
