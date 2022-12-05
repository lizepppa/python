class TreeNode:
    __slots__ = ['left', 'right', 'code', 'price']

    def __init__(self, code, price):
        self.left = None
        self.right = None
        if not isinstance(code, int) or code <= 0:
            raise TypeError("Item code should be an integer type!")
        if not isinstance(price, (int, float)) or price <= 0:
            raise TypeError("Item's price should be an integer or float type!")
        self.code = code
        self.price = price

    def insert(self, code, price):

        if not all(value > 0 for value in [code, price]):
            raise ValueError("Invalid input!")

        if self.code:
            if code < self.code:
                if not self.left:
                    self.left = TreeNode(code, price)
                else:
                    self.left.insert(code, price)

            elif code > self.code:
                if not self.right:
                    self.right = TreeNode(code, price)
                else:
                    self.right.insert(code, price)

    def find(self, code, volume):
        if not isinstance(volume, int):
            raise TypeError("Volume of items should be integer type value!")

        if not all(value > 0 for value in [code, volume]):
            raise ValueError("Invalid input!")

        if code == self.code:
            return self.price * volume

        elif code < self.code:
            if self.left:
                return self.left.find(code, volume)
        else:
            if self.right:
                return self.right.find(code, volume)
            raise ValueError("There are no item with given code!")


root = TreeNode(15, 54)
root.insert(10, 15)
root.insert(14, 13)
root.insert(20, 14.2)
root.insert(1, 22)
print(root.find(20, 10))
