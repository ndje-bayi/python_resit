
class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def __str__(self):
        return f"This is a {self.color} {self.model} from the year {self.year}"
    
toyota_sedan = Car("red", "Toyota sedan", "1999")
toyota_hilux = Car("white", "Toyota Hilux pick up", "2010")
honda = Car("blue", "Honda CRV cross-over",  "2007")

print (toyota_sedan)
print(toyota_hilux)
print(honda)
