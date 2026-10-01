class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("name:", self.name)
        print("color:", self.color)
        print("Starting the engine")


my_car = Car("Corolla", "Blue")
Car.start(my_car)
