from abc import ABC, abstractmethod


class Widget(ABC):
    @abstractmethod
    def render(self):
        pass


class Buttons(Widget):
    def render(self):
        pass


class TexBox(Widget):
    def render(self):
        pass


class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass


class MaterialWidgetFactory(WidgetFactory):
    def create_button(self):
        return MaterialButton()

    def create_textbox(self):
        return MaterialTextBox()


class MaterialButton(Buttons):

    def render(self):
        print("Material Button")


class MaterialTextBox(TexBox):
    def render(self):
        print("Material Textbox")


class AntWidgetFactory(WidgetFactory):

    def create_button(self):
        return AntButton()

    def create_textbox(self):
        return AndTextBox()


class AntButton(Buttons):

    def render(self):
        print("Ant Button")


class AndTextBox(TexBox):
    def render(self):
        print("Ant TextBox")


class ContactForm:
    """Client class"""
    def render(self, factory):
        factory.create_textbox().render()
        factory.create_button().render()


contact_form = ContactForm()
contact_form.render(MaterialWidgetFactory())
