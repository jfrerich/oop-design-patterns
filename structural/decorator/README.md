In this example, we have the following components:

- `Coffee` is the component interface that defines the operations that concrete
  coffee classes and decorators must implement.

- `SimpleCoffee` is a concrete component class that represents a simple coffee.

- `CoffeeDecorator` is an abstract decorator class that inherits from the
  `Coffee` component interface. It maintains a reference to an instance of the
  `Coffee` interface and provides a default implementation that delegates to
  the wrapped object.

- `MilkDecorator` and `SugarDecorator` are concrete decorator classes. They
  inherit from the `CoffeeDecorator` class and add additional behavior to the
  coffee.

In the usage example, we create an instance of the `SimpleCoffee` class,
representing a plain coffee. We can then decorate this simple coffee with
additional features using the decorator classes.

We start by creating a `MilkDecorator` object and passing the `SimpleCoffee`
instance to its constructor. This wraps the simple coffee with the milk
decorator, adding the cost and description of milk to the coffee.

Next, we create a `SugarDecorator` object and pass the previously decorated
coffee (milk coffee) to its constructor. This further wraps the coffee with the
sugar decorator, adding the cost and description of sugar to the coffee.

We can then call the `get_cost` and `get_description` methods on the decorated
coffee objects to retrieve the updated cost and description.

The Decorator pattern allows us to dynamically add new behavior or features to
an object without modifying its underlying class. We can apply multiple
decorators in any desired order to achieve the desired combination of features.
It provides a flexible and extensible way to enhance the functionality of
objects at runtime.

<img width="560" alt="image" src="https://github.com/jfrerich/oop-design-patterns/assets/7575921/1087d1b7-f58e-4d89-8a35-160ddd7dad14">

```python
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

```
