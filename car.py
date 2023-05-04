# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes 
# in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
  
    
class Car:
    strerring_wheel =1
    
    def __init__(self,make,model,colour):
        self.make = make
        self.model = model
        self.colour =colour
        
    def start(self):
        return f"{self.make} {self.model} has started"
    
    def stop(self):
        return f"The {self.colour} {self.make} has stopped the engine"
    
    def park(self):
        return f"The {self.colour} {self.model} has parked outside the house"
        
        