class Car:
    def method(self):
        print("super class")

class Sedan(Car):
    def method(self):
        print("surv class")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()
