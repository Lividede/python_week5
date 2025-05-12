# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self._power = power      # Encapsulated attribute
        self.level = level

    def show_identity(self):
        return f"I am {self.name}, my power is {self._power}."

    def fight_crime(self):
        return f"{self.name} is fighting crime with {self._power}!"

    def level_up(self):
        self.level += 1
        return f"{self.name} leveled up to {self.level}!"

# Derived class
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# Example usage
hero1 = Superhero("Bolt", "Electric Surge", 3)
hero2 = FlyingHero("Skyfire", "Solar Energy", 5, 800)

print(hero1.fight_crime())
print(hero2.show_identity())
print(hero2.fly())
print(hero2.level_up())
