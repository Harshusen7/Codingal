# create class
class Vehicle:
    # create init method
    def __init__(self, max_speed, mileage):
        # bind the aurguments
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("max speed :",self.max_speed)

# object creation
modelx = Vehicle(240, 18)
modelx.display()

# access the variable inside init method
print("model max speed:",modelx.max_speed)
print("model mileage:", modelx.mileage)
