from abc import ABC, abstractmethod


class Controller(ABC):
    """
        The Creator(Controller) class declares the factory method that is supposed to return an
        object of a Product class. The Creator's subclasses usually provide the
        implementation of this method.
    """
    def render(self, view_name, context):
        """Operation"""
        engine = self.create_view_engine()
        html = engine.render(view_name, context)
        return html

    @abstractmethod
    def create_view_engine(self):
        """Factory method"""
        pass


class SharpController(Controller):

    def create_view_engine(self):
        return SharpViewEngine()


class ProductsController(SharpController):

    def list_products(self):
        context = {}
        self.render("products.html", context)


class ViewEngine(ABC):
    @abstractmethod
    def render(self, view_name, context):
        pass


class MatchaViewEngine(ViewEngine):
    def render(self, view_name, context):
        print("View rendered by Matcha")


class SharpViewEngine(ViewEngine):

    def render(self, view_name, context):
        print("View rendered by Sharp")


control = ProductsController().list_products()

