class Vehicle:
    def move(self):
        print("Vehicle Moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Cycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

vehicle=[Vehicle(),Car(),Cycle()]

for v in vehicle:

    v.move()