class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    # Getters
    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def speed(self):
        return self.__speed

    # Setters
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @model.setter
    def model(self, model):
        self.__model = model

    @year.setter
    def year(self, year):
        self.__year = year

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    # Methods
    def increase_speed(self):
        self.__speed += 5
        return self.__speed

    def decrease_speed(self):
        self.__speed -= 5
        return self.__speed

    def stop(self):
        self.__speed = 0
        return self.__speed

    def display_speed(self):
        print(f"Текущая скорость: {self.__speed} км/ч")

    def reverse(self):
        self.__speed = -self.__speed
        return self.__speed
    

car = Car("Toyota", "Corolla", 2020)

car.display_speed()

print(car.increase_speed())
print(car.increase_speed())

print(car.decrease_speed())

print(car.reverse())

print(car.stop())

car.display_speed()