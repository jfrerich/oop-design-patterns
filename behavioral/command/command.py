
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
