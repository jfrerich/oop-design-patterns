'''Builder pattern is a solution to an anti-pattern called telescoping constructor.'''
'''Problem'''
'''  Excessive number of parameters to pass in the constructor, some of them are optional.'''
'''Scenario'''
''' A class needs to have a lot of optional parameters. It is not a good idea to pass all of them in the constructor. '''
'''Solution'''
''' Separate the construction of a complex object from its representation so that the same '''
''' construction process can create different representations.'''

# In this example, the Builder interface refers to the abstract builder class Builder. It defines
# the methods that concrete builder classes(SkyLarkBuilder and MustangBuilder) need
# to implement in order to build parts of the complex object(Car).

# The Builder class provides a blueprint for creating a Car object and keeps it as an
# attribute. It defines the create_new_car method, which creates a new instance of Car.

# The concrete builder classes (SkyLarkBuilder and MustangBuilder) inherit from the
# Builder class and implement the builder interface by providing their own
# implementations of the add_model, add_tires, and add_engine methods. These
# methods set the corresponding attributes of the Car object being built.

# The Director class is responsible for actually building the car. It takes a builder object as
# a parameter in its constructor and uses it to construct the car by calling the builder's
# methods. The Director class has a construct_car method that calls the builder's
# methods in a specific order to build the car. It also has a get_car method that returns the built Car object.

# The purpose of the builder interface and the Director class is to separate the
# construction of a complex object (Car) from its representation. The Director class
# controls the building process and uses the builder interface to delegate the construction to
# the appropriate concrete builder. This allows for flexibility in constructing different variations
# of the complex object using the same building process.


class Director:
    '''Director Class - Actually builds the car'''

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()  # create new car object
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    '''Abstract builder class'''
    '''Builder Class - creates a Car object and keeps it as an attribute'''

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class Car:
    '''Product class - defines the complex object to be created'''

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


class SkyLarkBuilder(Builder):
    '''Concrete builder class - inherits the abstract builder class and implements the builder interface'''
    '''implements the builder interface to build parts of the complex object'''

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class MustangBuilder(Builder):
    '''Concrete builder class inherits the abstract builder class and implements the builder interface'''
    '''provides parts and tools to work on the parts'''
    '''implements the builder interface to build parts of the complex object'''

    def add_model(self):
        self.car.model = "Mustang"

    def add_tires(self):
        self.car.tires = "Race tires"

    def add_engine(self):
        self.car.engine = "5.0 engine"


mustang_builder = MustangBuilder()  # concrete builder
skylark_builder = SkyLarkBuilder()  # concrete builder
# director object takes the concrete builder and puts it to work
director = Director(skylark_builder)
director.construct_car()
car = director.get_car()
print(car)

director = Director(mustang_builder)
director.construct_car()
car = director.get_car()
print(car)
