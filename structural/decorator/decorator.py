from functools import wraps

'''decorator is a function that takes another function and extends the 
   behavior of the latter function without explicitly modifying it.'''


def make_blink(function):
    """Defines the decorator"""
    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()
        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"
    return decorator


@make_blink
# Apply the decorator here!
def hello_world():
    """Original function! """
    return "Hello, World!"


print(hello_world())


class Coffee:
    """Component interface"""

    def get_cost(self):
        pass

    def get_description(self):
        pass


class SimpleCoffee(Coffee):
    """Concrete component representing a simple coffee"""

    def get_cost(self):
        return 1.0

    def get_description(self):
        return "Simple Coffee"


class CoffeeDecorator(Coffee):
    """Decorator abstract class"""

    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost()

    def get_description(self):
        return self.coffee.get_description()


class MilkDecorator(CoffeeDecorator):
    """Concrete decorator that adds milk to the coffee"""

    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 0.5

    def get_description(self):
        return super().get_description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    """Concrete decorator that adds sugar to the coffee"""

    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 0.2

    def get_description(self):
        return super().get_description() + ", Sugar"


# Usage example
simple_coffee = SimpleCoffee()
print(simple_coffee.get_description())  # Output: Simple Coffee
print(simple_coffee.get_cost())  # Output: 1.0

milk_coffee = MilkDecorator(simple_coffee)
print(milk_coffee.get_description())  # Output: Simple Coffee, Milk
print(milk_coffee.get_cost())  # Output: 1.5

sugar_milk_coffee = SugarDecorator(milk_coffee)
# Output: Simple Coffee, Milk, Sugar
print(sugar_milk_coffee.get_description())
print(sugar_milk_coffee.get_cost())  # Output: 1.7
