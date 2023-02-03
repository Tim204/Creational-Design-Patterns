from abc import ABC, abstractmethod

class Slide:

    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text


class Presentation:

    def __init__(self):
        self.slides = []

    def add_slide(self, slide):
        self.slides.append(slide)

    def export(self, builder):
        builder.add_slide(Slide("Copyrite"))
        for slide in self.slides:
            builder.add_slide(slide)


class PresentationBuilder(ABC):
    @abstractmethod
    def add_slide(self, slide):
        pass


class PdfDocument:

    def add_page(self, text):
        print("Adding a page to PDF")


class PdfDocumentBuilder(PresentationBuilder):

    document = PdfDocument()

    def add_slide(self, slide):
        self.document.add_page(slide.get_text())


class Movie:

    def add_frame(self, text, duration):
        print("Adding a frame to the Movie")


class MovieBuilder(PresentationBuilder):

    movie = Movie()

    def add_slide(self, slide):
        self.movie.add_frame(slide.get_text(), duration=3)


def client():
    presentation = Presentation()
    presentation.add_slide(Slide("Slide 1"))
    presentation.add_slide(Slide("Slide 2"))

    presentation.export(MovieBuilder())


client()