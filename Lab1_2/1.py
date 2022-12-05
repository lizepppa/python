class Rectangle:
    def __init__(self,length=1,width=1):
        self.length=length
        self.width=width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, s):
        if not isinstance(s, (int,float)):
            raise TypeError("Length must be number!")
        if s < 0 or s > 20:
            raise ValueError("Length cant be lesser than zero or bigger then twenty!")
        self.__length = s

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, s):
        if not isinstance(s, (int,float)):
            raise TypeError("width must be number!")
        if s < 0 or s > 20
            raise ValueError("width cant be lesser than zero or bigger then twenty!")
        self.__width = s

    def perimeter(self):
        return (self.length+self.width)*2

    def area(self):
        return self.length*self.width


rect = Rectangle(20,3)
print(rect.perimeter())
print(rect.area())
