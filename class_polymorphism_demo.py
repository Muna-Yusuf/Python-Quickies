# Assignment 1: Class Design
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
    
    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def battery_status(self):
        print(f"Battery life: {self.battery_life}%")

# Inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system
    
    def enable_game_mode(self):
        print(f"Game mode enabled on {self.model} with {self.cooling_system} cooling!")

# Testing
phone = Smartphone("Apple", "iPhone 14", 80)
phone.call("123456789")
phone.battery_status()

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 90, "Liquid Cooling")
gaming_phone.enable_game_mode()
gaming_phone.battery_status()

# Assignment 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
