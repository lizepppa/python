from abc import abstractmethod


class ICourse():
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ILocalCourse(ICourse):
    @property
    @abstractmethod
    def room(self):
        pass

    @room.setter
    @abstractmethod
    def room(self, value):
        pass


class IOffsiteCourse(ICourse):
    @property
    @abstractmethod
    def town(self):
        pass

    @town.setter
    @abstractmethod
    def town(self, value):
        pass


class ITeacher:
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @courses.setter
    @abstractmethod
    def courses(self, value):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Course(ICourse):
    def __init__(self, name, teacher, program):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be str')
        if not value.strip():
            raise ValueError('name can\'t be empty')
        self.__name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError('teacher must be Teacher type')
        self.__teacher = value

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        if not isinstance(value, str):
            raise TypeError('program must be str type')
        self.__program = value

    def __str__(self) -> str:
        return f'Local course: {self.name}, Teacher: {self.teacher.name}, Program: {self.program}'


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, room, program):
        self.room = room
        super().__init__(name, teacher, program)

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        if not isinstance(value, str):
            raise TypeError('room must be str type')
        self.__room = value

    def __str__(self) -> str:
        return f'Local course: {self.name}, Room: {self.room}, Teacher: {self.teacher.name}, Program: {self.program}'


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name, teacher, town, program):
        self.town = town
        super().__init__(name, teacher, program)

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, value):
        if not isinstance(value, str):
            raise TypeError('town must be str type')
        self.__town = value

    def __str__(self) -> str:
        return f'Offsite course: {self.name}, Town: {self.town}, Teacher: {self.teacher.name}, Program: {self.program}'


class Teacher(ITeacher):
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be str')
        if not value.strip():
            raise ValueError('name can\'t be empty')
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not isinstance(value, str):
            raise TypeError('courses must be str')
        self.__courses = value

    def __str__(self) -> str:
        return f'Teacher: {self.name}  Courses: {self.courses}'

def main():
    x = Teacher('Boris', 'c++, java')
    w = Teacher('Evgenij', 'php')
    y = LocalCourse('C++ course', x, 'room #1', 'syntax and procedure programing')
    z = OffsiteCourse('Java course', x, 'Kyiv', 'base of oop')

    print(x)
    print(y)
    print(w)
    print(z)

if __name__ == '__main__':
    main()
