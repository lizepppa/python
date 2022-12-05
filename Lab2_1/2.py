import json
import os
import dataclasses
from datetime import datetime

BASE_PRICE = 100
ADDON_PRICE = 5


class Kitchen:
    """Class for getting info on ingredients quantity, storing it and handling order creation"""
    def __init__(self, stock_info, log_input):
        if not os.path.isfile(stock_info):
            raise ValueError("Kitchen stock info doesnt exist")
        self.file_name = stock_info
        self.log_name = log_input
        with open(stock_info, "r") as inp:
            self.__stock_info = json.load(inp)
        self.today_orders = []

    def __del__(self):
        """Update info on used products"""
        with open(self.file_name, "w") as upd:
            json.dump(self.__stock_info, upd, indent=4)
        with open(self.log_name, "w") as log:
            json.dump(self.today_orders, log, indent=4)

    def available_addons(self, customer):
        """Getting info on available addons based on day of the week and ingredients availability"""
        addons = []
        base_required = dataclasses.asdict(self.get_order(customer, True))
        for keys in self.__stock_info.keys():
            if self.__stock_info[keys] > 1:
                if self.__stock_info[keys] - base_required[keys] > 0:
                    addons.append((keys, self.__stock_info[keys]))
        return addons

    def get_order(self, customer, *check, **kwargs):
        """Create an order and subtract used up ingredients"""
        if not isinstance(customer, Customer):
            raise TypeError("Client should be customer type")
        price = BASE_PRICE + len(kwargs)*ADDON_PRICE
        match customer.date.weekday():
            case 0:
                obj = Mondaypizza(price, **kwargs)
            case 1:
                obj = Tuesdaypizza(price, **kwargs)
            case 2:
                obj = Wednesdaypizza(price, **kwargs)
            case 3:
                obj = Thursdaypizza(price, **kwargs)
            case 4:
                obj = Fridaypizza(price, **kwargs)
            case _:
                obj = Weekendpizza(price, **kwargs)
        required = dataclasses.asdict(obj)
        if not check:
            for keys in required.keys():
                if keys == 'price':
                    continue
                self.__stock_info[keys] -= required[keys]
                if self.__stock_info[keys] < 0:
                    raise ValueError("Required products not in stock")
            self.today_orders.append(dataclasses.asdict(obj))
        return obj


@dataclasses.dataclass(frozen=True)
class Customer:
    """Class for storing info about a client"""
    name: str
    date: datetime


@dataclasses.dataclass(frozen=True)
class Pizzabase:
    """Base class storing info about pizza"""
    price: int
    sauce: int = 1
    cheese: int = 1
    beef: int = 0
    bbq_sauce: int = 0
    pepperoni: int = 0
    pepper: int = 0
    blue_cheese: int = 0
    ham: int = 0
    mushrooms: int = 0
    feta_cheese: int = 0
    cheddar_cheese: int = 0
    pork: int = 0
    sausage: int = 0
    bacon: int = 0

    def __str__(self):
        dictionary = dataclasses.asdict(self)
        return '  '.join([key+' '+str(dictionary[key]) for key in dictionary.keys() if dictionary[key]])


@dataclasses.dataclass(frozen=True, kw_only=True)
class Mondaypizza(Pizzabase):
    pepperoni: int = 1
    pepper: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class Tuesdaypizza(Pizzabase):
    pepperoni: int = 1
    blue_cheese: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class Wednesdaypizza(Pizzabase):
    beef: int = 1
    bbq_sauce: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class Thursdaypizza(Pizzabase):
    ham: int = 1
    mushrooms: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class Fridaypizza(Pizzabase):
    blue_cheese: int = 1
    feta_cheese: int = 1
    cheddar_cheese: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class Weekendpizza(Pizzabase):
    beef: int = 1
    pork: int = 1
    sausage: int = 1
    bacon: int = 1


def main():
    file = "kitchen.json"
    log = "used_ingredients.json"
    rest = Kitchen(file, log)
    maks = Customer("Maksim", datetime.now())
    print(rest.available_addons(maks))
    order = rest.get_order(maks, ham=1, pork=1)
    print(order)


if __name__ == '__main__':
    main()


kitchen.json 
{
    "sauce": 13,
    "cheese": 13,
    "pepperoni": 18,
    "pepper": 19,
    "blue_cheese": 19,
    "beef": 15,
    "bbq_sauce": 15,
    "ham": 14,
    "mushrooms": 20,
    "feta_cheese": 20,
    "cheddar_cheese": 20,
    "pork": 14,
    "sausage": 20,
    "bacon": 20
}


used_ingredients.json
{
}