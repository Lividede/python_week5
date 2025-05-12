class Vehicle:
    def move(self):
        pass  # Abstract behavior

class Car(Vehicle):
    def move(self):
        return "Driving on the road."

class Plane(Vehicle):
    def move(self):
        return "Flying through the skies."

class Boat(Vehicle):
    def move(self):
        return "Sailing on water."

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
