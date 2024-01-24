#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystype):
        self.bodytype = bodystype 

    def drive(self, speed):
        self.mode = "Driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheel = 4
        self.door = 4
        self.enginetype = enginetype
    
    def drive(self,speed):
        super().drive(speed)
        print(self.mode,"my", self.enginetype, "car at", self.speed, "speed")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, sideCar):
        super().__init__("Motocycle")
        self.enginetype = enginetype
        self.sideCar = sideCar

        if (sideCar):
            self.wheel = 3
        else:
            self.wheel = 2

    def drive(self, speed):
        super().drive(speed)
        print(self.mode, self.enginetype, "motorbike at" , self.speed, "speed")


car1 = Car('gas')
car2 = Car("electric")
mc = Motorcycle('gas', True)


print(car1.enginetype)
print(car2.door)
print(mc.enginetype)
print(mc.wheel)

print(car1.drive(50))
print(mc.drive(90))