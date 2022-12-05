class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, s):
        if not isinstance(s, int):
            raise TypeError("price must be integer")
        elif s < 0:
            raise ValueError("price cant be lesser than zero")
        self.__price = s

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,descr):
        if not isinstance(descr, str):
            raise TypeError("description must be string")
        self.__description =  descr

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self,dim):
        if not isinstance(dim, str):
            raise TypeError("dimensions must be string")
        self.__dimensions = dim


class Customer:
    def __init__(self, name, surname, telephone):
        self.name = name
        self.surname = surname
        self.telephone = telephone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if not isinstance(n, str):
            raise TypeError("name must be string")
        self.__name = n

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, n):
        if not isinstance(n, str):
            raise TypeError("surname must be string")
        self.__surname = n

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, n):
        if not isinstance(n, str):
            raise TypeError("surname must be string")
        self.__telephone = n


class Order(object):
    def __init__(self, customer, *args):
        self.customer = customer
        self.args = args

    def sum(self):
        num = 0
        for x in self.args:
            num += x.price
        return num

    def products_info(self):
        for x in self.args:
            print(x.price, x.description, x.dimensions)

    def customer_info(self):
        return (self.customer.name, self.customer.surname, self.customer.telephone)


Buyer = Customer("Ivan", "Ivanovich", "+380965194692")
prod1 = Product(211, "Chair", "300x200x100")
prod2 = Product(1000, "table", "500x250x100")
prod3 = Product(1020, "table", "500x250x100")
ord = Order(Buyer, prod1, prod2, prod3)
print(ord.sum())
ord.products_info()
print(ord.customer_info())
