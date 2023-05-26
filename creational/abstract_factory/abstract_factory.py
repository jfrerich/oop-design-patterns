from abc import ABC, abstractmethod


class Button(ABC):
    # Abstract Product A
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    # Concrete Product A1
    def paint(self):
        return "Rendering a button in a Windows style."


class MacOSButton(Button):
    # Concrete Product A2
    def paint(self):
        return "Rendering a button in a MacOS style."


class Checkbox(ABC):
    # Abstract Product B
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):
    # Concrete Product B1
    def paint(self):
        return "Rendering a checkbox in a Windows style."


class MacOSCheckbox(Checkbox):
    # Concrete Product B2
    def paint(self):
        return "Rendering a checkbox in a MacOS style."


class GUIFactory(ABC):
    # Abstract Factory
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    # Concrete Factory 1
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    # Concrete Factory 2
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
