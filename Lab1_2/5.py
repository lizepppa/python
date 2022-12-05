class Student:
    def __init__(self, name, surname, math, eng, pe):
        self.name = name
        self.surname = surname
        self.math = math
        self.eng = eng
        self.pe = pe

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, s):
        if not isinstance(s, str) or len(s) < 3:
            raise TypeError("Normal name pls")
        self.__name = s

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, s):
        if not isinstance(s, str) or len(s) < 3:
            raise TypeError("Normal surname pls")
        self.__surname = s

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, val):
        if not isinstance(val, int) or val < 1 or val > 12:
            raise TypeError("Input correct grade")
        self.__math = val

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, val):
        if not isinstance(val, int) or val < 1 or val > 12:
            raise TypeError("Input correct grade")
        self.__eng = val

    @property
    def pe(self):
        return self.__pe

    @pe.setter
    def pe(self, val):
        if not isinstance(val, int) or val < 1 or val > 12:
            raise TypeError("Input correct grade")
        self.__pe = val


class group(object):
    def __init__(self, name, *args):
        self.name = name
        self.students = sorted(args, key=lambda student: student.surname, reverse=False)

    def show(self):
        print(" Surname      Name      Math Eng Pe")
        for x in self.students:
            print("{0:10}".format(x.surname) + "{0:13}".format(x.name) + "{0:3} ".format(x.math) + "{0:3} ".format(
                x.eng) + "{0:3} ".format(x.pe))

    def best_stud(self):
        print(" Surname      Name      Aver")
        for x in sorted(self.students, key=lambda student: student.math, reverse=True):
            print("{0:10}".format(x.surname) + "{0:13}".format(x.name) + "{0:3} ".format(
                round(((x.math + x.pe + x.eng) / 3), 2)))


liza = Student("Liza", "Plohuta", 11, 10, 10)
agata = Student("Agata", "Kryvokon`", 1, 1, 1)
katya = Student("Katya", "Pihovkina", 4, 12, 7)
tv12 = group("tv12", liza, agata,  katya)
tv12.best_stud()
tv12.show()
