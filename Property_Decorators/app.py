class Product:
    def __init__(self,_price):
        self._price = _price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

p = Product(100)        # Create object with price 100
print(p.price)          # Calls the @property method → prints 100

p.price = 150           # Calls the @price.setter → updates price to 150
print(p.price)          # Prints 150

del p.price             # Calls the @price.deleter → deletes _price
