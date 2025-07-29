from .base import Element, VoidElement


class Div(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("div", *args, **kwargs)


class P(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("p", *args, **kwargs)


class Span(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("span", *args, **kwargs)


class A(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("a", *args, **kwargs)


class Strong(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("strong", *args, **kwargs)


class Em(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("em", *args, **kwargs)


class H1(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h1", *args, **kwargs)


class H2(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h2", *args, **kwargs)


class H3(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h3", *args, **kwargs)


class H4(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h4", *args, **kwargs)


class H5(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h5", *args, **kwargs)


class H6(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h6", *args, **kwargs)


class Ul(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("ul", *args, **kwargs)


class Ol(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("ol", *args, **kwargs)


class Li(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("li", *args, **kwargs)


class Table(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("table", *args, **kwargs)


class Thead(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("thead", *args, **kwargs)


class Tbody(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("tbody", *args, **kwargs)


class Tr(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("tr", *args, **kwargs)


class Th(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("th", *args, **kwargs)


class Td(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("td", *args, **kwargs)


class Form(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("form", *args, **kwargs)


class Label(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("label", *args, **kwargs)


class Button(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("button", *args, **kwargs)


class Section(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("section", *args, **kwargs)


class Header(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("header", *args, **kwargs)


class Footer(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("footer", *args, **kwargs)


class Nav(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("nav", *args, **kwargs)


class Main(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("main", *args, **kwargs)


class Article(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("article", *args, **kwargs)


class Aside(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("aside", *args, **kwargs)


class Html(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("html", *args, **kwargs)


class Head(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("head", *args, **kwargs)


class Body(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("body", *args, **kwargs)


class Title(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("title", *args, **kwargs)


class Script(Element):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("script", *args, **kwargs)


class Img(VoidElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("img", *args, **kwargs)


class Br(VoidElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("br", *args, **kwargs)


class Hr(VoidElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("hr", *args, **kwargs)


class Input(VoidElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("input", *args, **kwargs)


class Link(VoidElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("link", *args, **kwargs)


class Meta(VoidElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("meta", *args, **kwargs)
