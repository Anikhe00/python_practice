#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
class Pizza:
    def __init__(self, size, crust_type, toppings):
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings if toppings is not None else []
        
    # 2. Add a method to add a new topping
    def add_topping(self, topping):
        self.toppings.append(topping)
        
    # 3. Add a method to remove a topping if it exists
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            
    # 4. Add a method to print pizza details:
    #    - size, crust, and all toppings (or “No toppings yet!”)
    def print_pizza_details(self):
        print("=== 🍕 Pizza Details 🍕 ===")
        print(f"Size: {self.size}")
        print(f"Crust type: {self.crust_type}")
        if self.toppings:
            print("Toppings:", ", ".join(self.toppings))
        else:
            print("No toppings yet!")

# 5. Create a pizza object, customize it, and print the summary
my_pizza = Pizza("Large", "Thin Crust", ["Cheese"])
my_pizza.add_topping("Cheese")
my_pizza.add_topping("Pepperoni")
my_pizza.add_topping("Olives")
my_pizza.remove_topping("Pineapple")
my_pizza.remove_topping("Cheese")
my_pizza.print_pizza_details()