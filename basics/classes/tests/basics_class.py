print("Hello World!")
print("I am on github!")


class Car:
    class_attribute = "I am a class attribute"

    def __init__(self, name, speed=0  # default value for speed
                 ):
        self.name = name
        self.speed = speed

    def print_name(self):
        print(self.name)


obj1 = Car("Car 1!")
obj1.print_name()
obj1.class_attribute = "I am a new class attribute"
print(obj1.class_attribute)  # I am a new class attribute
print(Car.class_attribute)  # I am a class attribute

obj2 = Car("Car 2!")
obj2.print_name()
print(obj2.class_attribute)  # I am a class attribute
print(Car.class_attribute)  # I am a class attribute


obj_attributes = dir(obj1)
print(obj_attributes)