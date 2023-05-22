'''
In this example, we have an abstract Command interface that defines the execute
method. Concrete command classes (LightOnCommand and LightOffCommand) implement
this interface and provide their own implementations of the execute method.

The Light class is the receiver class, which contains the actual functionality
that needs to be performed. It has on and off methods to control the light.

The LightOnCommand and LightOffCommand classes are concrete command classes
that encapsulate the receiver's methods. They take an instance of the Light
class as a parameter in their constructors and call the corresponding methods
(on or off) of the receiver in their execute methods.

The RemoteControl class is the invoker class. It holds a dictionary of
commands, where the slot number is the key and the command object is the value.
The set_command method is used to set the command for a particular slot. The
press_button method takes a slot number as a parameter and executes the
corresponding command if it exists in the dictionary.

In the usage example, we create an instance of the Light class and two
instances of the concrete command classes: LightOnCommand and LightOffCommand.
We then create an instance of the RemoteControl class and set the commands for
two slots (0 and 1).

When we call remote_control.press_button(0), the LightOnCommand associated with
slot 0 is executed, and the light is turned on. Similarly, when we call
remote_control.press_button(1), the LightOffCommand associated with slot 1 is
executed, and the light is turned off.

The Command pattern decouples the invoker from the receiver, allowing different
commands to be assigned to different slots and executed when desired. It
provides a way to encapsulate and parameterize actions, making it easier to
implement functionality such as undo/redo, logging, or macro
recording/playback.
'''


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
