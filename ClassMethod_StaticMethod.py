# Python program to demonstrate
# use of class method and static method.

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)


class Person2():
    species = 'homo_sapiens' # This is class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Name: {}, age: {}.'.format(self.name, date.today().year - self.age))

    @classmethod
    def create_with_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    @staticmethod
    def get_birth_year(age):
        return date.today().year - age


if __name__ == "__main__":
    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.isAdult(22))
    # print(person1.isAdult())

# """""""""""""""""""""""""""""""""""
# If you created a staticmethod within a class,
# you don't need to create an instance of the class before using the staticmethod.
