🎯 Topic 2: Benefits of OOP
✅ Key Advantages
Modularity

Classes act as independent modules.

Example: Separate User and Product classes in an e-commerce app.

Reusability

Inherit from base classes (e.g., Animal → Dog/Cat).

Use libraries/packages built with OOP.

Scalability

Easily extend functionality without breaking existing code.

Example: Add ElectricCar subclass to a Vehicle hierarchy.

Data Hiding

Protect sensitive data via private attributes (e.g., __password).

Expose only necessary methods (getters/setters).

Readability

Clear structure with intuitive class/method names.

Example: employee.calculate_salary() vs procedural code.

🧪 Practical Example: Vehicle Class
python
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed  # Protected attribute

    def display_info(self):
        print(f"{self.brand} (Max Speed: {self._max_speed} km/h)")

# Usage
car = Vehicle("Tesla", 250)
car.display_info()  # Output: "Tesla (Max Speed: 250 km/h)"
⚠️ Common Pitfalls
Over-engineering: Not all problems need OOP.

Deep Inheritance: Favor composition over deep hierarchies.