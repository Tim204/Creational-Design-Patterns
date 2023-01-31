import copy
from abc import ABC, abstractmethod


class Component(ABC):
    """Prototype"""
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class Circle(Component):
    """Concrete Prototype"""

    def __init__(self, radius):
        self._radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def render(self):
        print(f"Rending a circle with a radius of {self._radius}cm")


class Rectangle(Component):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def render(self):
        print(f"Rendering rectangle with dimension {self.breath, self.length}")

    def clone(self):
        return copy.deepcopy(self)


class ContextMenu:
    """Client"""

    def duplicate(self, component):
        new_component = component.clone()
        new_component.render()


rectangle = Rectangle(10, 5)
circle = Circle(12)

prot = ContextMenu()
prot.duplicate(circle)




