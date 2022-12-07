class Person:
    def __init__(self, name, surname, phone, birthday):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone

    @property
    def birthday(self):
        return self.__birthday

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('name must be a string')
        if not val.strip():
            raise ValueError('name is empty')
        self.__name = val.strip()

    @surname.setter
    def surname(self, val):
        if not isinstance(val, str):
            raise TypeError('surname must be a string')
        if not val.strip():
            raise ValueError('surname is empty')
        self.__surname = val.strip()

    @phone.setter
    def phone(self, val):
        if not isinstance(val, str):
            raise TypeError('phone must be a string')
        if not val.strip():
            raise ValueError('phone is empty')
        self.__phone = val

    @birthday.setter
    def birthday(self, val):
        if not isinstance(val, str):
            raise TypeError('birthday must be a string')
        if not val.strip():
            raise ValueError('birthday is empty')
        self.__birthday = val

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__phone} {self.__birthday}'


class Notebook:
    def __init__(self, *args):
        self.records = list(args)

    @property
    def records(self):
        return self.__records

    @records.setter
    def records(self, val):
        if not all(isinstance(x, Person) for x in val):
            raise TypeError('person must be Person type')
        self.__records = val

    def __add__(self, other):
        if not isinstance(other, Person):
            raise TypeError('person must be Person type')
        self.__records.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, Person):
            raise TypeError('person must be Person type')
        self.__records.remove(other)
        return self

    def __mul__(self, val):
        if not isinstance(val, str):
            raise TypeError('searching field must be str')
        for rec in self.__records:
            if rec.name == val or rec.surname == val or rec.phone == val or rec.birthday == val:
                return rec

    def __str__(self):
        return '\n'.join([str(x) for x in self.__records])


def main():
    person1 = Person('Elizaveta', 'Plohuta', '+380961921937', '23.08.2004')
    person2 = Person('Angelina', 'Zablovskaya', '+380961921945', '18.10.2004')
    y = Notebook(person1, person2)
    print(y * 'Elizaveta')


if __name__ == '__main__':
    main()
