In this example, we have the following components:

- `Subject` represents the subject or the object being observed. It maintains a
  list of observers and provides methods to attach, detach, and notify the
  observers.

- `Observer` is the base observer class that defines the interface for
  receiving updates from the subject.

- `ConcreteObserver` is a concrete observer class that implements the `update`
  method to receive and process updates from the subject.

In the usage example, we create an instance of the `Subject` class. Then we
create three instances of the `ConcreteObserver` class representing the
observers.

We attach all three observers to the subject using the `attach` method. This
means that they will start receiving notifications from the subject.

We then call the `notify` method on the subject, passing a message as an
argument. This triggers the `update` method on each attached observer, and they
receive and process the message.

Next, we detach `observer2` from the subject using the `detach` method. This
means that `observer2` will no longer receive notifications from the subject.

Finally, we call the `notify` method again on the subject, and only `observer1`
and `observer3` receive the updated message.

The Observer pattern allows for loose coupling between subjects and observers.
Multiple observers can be attached to a subject, and they will be notified
automatically whenever the subject's state changes. This enables a one-to-many
relationship between the subject and its observers, facilitating event-driven
systems and decoupled architectures.

<img width="571" alt="image" src="https://github.com/jfrerich/oop-design-patterns/assets/7575921/370b19e9-e05c-4438-beb4-c731ad7516ee">

```python
class Subject:
    """Subject class"""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    """Observer class"""

    def update(self, message):
        pass


class ConcreteObserver(Observer):
    """Concrete observer class"""

    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")


# Usage example
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")
observer3 = ConcreteObserver("Observer 3")

subject.attach(observer1)
subject.attach(observer2)
subject.attach(observer3)

subject.notify("Hello, observers!")

subject.detach(observer2)

subject.notify("Observer 2 detached")

```


