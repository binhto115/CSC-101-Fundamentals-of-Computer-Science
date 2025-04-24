class Vehicle:
    def __init__(self, wheels: int, fuelremaining: str, doors: int, roof: str):
        self.wheels = wheels
        self.fuelremaining = fuelremaining
        self.doors = doors
        self.roof = roof
    def __str__(self):
        return "Vehicle Check: (%f, %f, %f, %f)" % (self.wheels, self.fuelremaining, self.doors, self.roof)

