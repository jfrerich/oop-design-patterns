# Abstract Factory Pattern

In this example, we have the following components:

- Abstract Product A (`Button`): Declares an interface for a button.
- Concrete Product A1 (`WindowsButton`): Implements the Windows-specific
  button.
- Concrete Product A2 (`MacOSButton`): Implements the MacOS-specific button.
- Abstract Product B (`Checkbox`): Declares an interface for a checkbox.
- Concrete Product B1 (`WindowsCheckbox`): Implements the Windows-specific
  checkbox.
- Concrete Product B2 (`MacOSCheckbox`): Implements the MacOS-specific
  checkbox.
- Abstract Factory (`GUIFactory`): Declares an interface for creating the
  abstract products.
- Concrete Factory 1 (`WindowsFactory`): Implements the creation of
  Windows-specific products.
- Concrete Factory 2 (`MacOSFactory`): Implements the creation of
  MacOS-specific products.

The client code uses the abstract factory to create a family of related
products (a button and a checkbox) without specifying their concrete classes.
It simply works with the abstract interfaces (`Button` and `Checkbox`).
Depending on which factory is passed to the `create_gui` function, the
appropriate concrete products are created and used.

This way, the client code remains decoupled from the specific product classes
and can easily switch between different product families (e.g., Windows or
MacOS) by using the corresponding factory. The Abstract Factory pattern enables
the creation of families of related objects while maintaining a consistent
interface.

```python
from abc import ABC, abstractmethod

# Abstract Product A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Product A1
class WindowsButton(Button):
    def paint(self):
        return "Rendering a button in a Windows style."

# Concrete Product A2
class MacOSButton(Button):
    def paint(self):
        return "Rendering a button in a MacOS style."

# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in a Windows style."

# Concrete Product B2
class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in a MacOS style."

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory 1
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory 2
class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Client code
def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.paint())
    print(checkbox.paint())

# Usage
create_gui(WindowsFactory())  # Renders a Windows-styled button and checkbox

create_gui(MacOSFactory())  # Renders a MacOS-styled button and checkbox
```
