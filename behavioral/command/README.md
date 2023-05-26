# Command Pattern

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
class Command:
    '''Command interface'''

    def execute(self):
        pass


class Light:
    '''Receiver class'''

    def on(self):
        print("light is on.")

    def off(self):
        print("light is off.")

    def blow_up(self):
        print("light is blown up.")


class LightOnCommand(Command):
    '''Concrete command that turns on the light'''

    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.on()


class LightOffCommand(Command):
    '''Concrete command that turns off the light'''

    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.off()


class LightBlowUpCommand(Command):
    '''Concrete command that blows up the light'''

    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.blow_up()


class RemoteControl:
    '''Invoker class'''

    def __init__(self):
        self.commands = {}

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            self.commands[slot].execute()


# Usage example
'''
In the example provided, the "client" would typically be the code that utilizes
the Command pattern to achieve a specific behavior or functionality. In this
case, the usage example at the bottom of the code can be considered the client
code. '''
light = Light()

light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)
light_blow_up_command = LightBlowUpCommand(light)

remote_control = RemoteControl()
remote_control.set_command(0, light_on_command)
remote_control.set_command(1, light_off_command)
remote_control.set_command(2, light_blow_up_command)

remote_control.press_button(0)
remote_control.press_button(1)
remote_control.press_button(2)
```
