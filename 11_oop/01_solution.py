# Generalized Class
class Car:
# Class variable
    Total_car = 0

# __init__ is called constructor and self is used for communication b/w class and instance
    def __init__(self, Brand, Model):
        self.__Brand = Brand
        self.__Model = Model
        Car.Total_car += 1



# adding method
    def full_name(self):
        return f"{self.__Brand} {self.__Model}"




# Encapsulation
    def get_Brand(self):
# __Brand makes Brand attribute private
        return self.__Brand + "!"
    


# polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    


# Static method
    @staticmethod
    def general_description():
        return "Cars are Modes of Transport"
    


# Property decorator
    @property   
    def model(self):
        return self.__Model




# Inheritance(Taking value/ reference from parent class)
class ElectricCar(Car):
    def __init__(self , Brand, Model, Battery_size):
        super().__init__(Brand, Model)
        self.Battery_size = Battery_size

# polymorphism
    def fuel_type(self):
        return "Electric charge"

    
    def full_name2(self):
        return f"{self.__Brand} {self.Model} {self.Battery_size}"
    



    

my_electric_car = ElectricCar("Tesla" , "Model S" , "85 kWh")

print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))
# print(my_electric_car.get_Brand())
# print(my_electric_car.Model)
# print(my_electric_car.Battery_size)
# print(my_electric_car.fuel_type())
# print(my_electric_car.full_name2())

class Battery:
    def B_info(self):
        return "Battery of car is 10PH"
    

class Engine:
    def E_info(self):
        return "Engine of car is V4"    
    
class ElectricCar2(Battery, Engine, Car):
    pass

my_new = ElectricCar2("Tesla" , "Model s1")
print(my_new.B_info())
print(my_new.E_info())








# Instance
my_car = Car("Toyota" , "Corolla")


print(my_car.get_Brand())
# print(my_car.Model)
# print(my_car.full_name())
# print(my_car.fuel_type())
# print(Car.Total_car)
# print(Car.general_description())
print(my_car.model)



my_new_car = Car("Tata" , "Nexon")

# print(my_new_car.get_Brand())
# print(my_new_car.Model)



# getter and setter method

class Child:
    
    def self_age(self, age = 0):
        self._age = age

# get method
    def get_age(self):
        return self._age
    
# set method
    def set_age(self , x):
        self._age = x

Hoor = Child()

Hoor.set_age(4)

print(Hoor._age)
print(Hoor.get_age())




