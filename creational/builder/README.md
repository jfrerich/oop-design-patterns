# Builder Pattern

In this example, we have the following classes:

- `Director`: This class is responsible for the construction process and works
  with the provided builder interface. It calls the builder's methods to
  construct the product step by step.

- `Builder`: This class defines the interface for building the product. It
  includes abstract methods for building different parts of the product and a
  method for retrieving the final result.

- `ConcreteBuilder`: This class implements the Builder interface and provides
  the concrete implementation for building the product. It maintains an
  instance of the product being built and defines the specific building steps.

- `Product`: This class represents the final product being constructed. It
  contains the parts of the product and provides methods for adding parts and
  listing them.

In the client code, we create an instance of the ConcreteBuilder and pass it to
the Director. The Director then orchestrates the construction process by
calling the builder's methods. Finally, we retrieve the constructed product
from the builder and demonstrate its parts.

This design allows you to separate the construction logic from the product
itself, providing a flexible and extensible way to create complex objects with
different variations.

<img width="607" alt="image" src="https://github.com/jfrerich/oop-design-patterns/assets/7575921/11b2467f-f4c7-4a74-916d-e20839340c6e">


```python
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A")

    def build_part_b(self):
        self.product.add_part("Part B")

    def build_part_c(self):
        self.product.add_part("Part C")

    def get_result(self):
        return self.product

class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)


# Client code
builder = ConcreteBuilder()
director = Director(builder)

director.construct()
product = builder.get_result()

print("Parts of the product:", product.list_parts())
```
