class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"{self.year}: {self.brand} is starting...")

    def stop(self):
        print(f"{self.year}: {self.brand} is stoping...")

c = Car("BMW",2023)
c.start()
c.stop()