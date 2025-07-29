from typing import Union
from .base import Element, VoidElement


def h(tag: str, *args, **kwargs) -> Union[Element, VoidElement]:
    void_elements = ["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]
    if tag in void_elements:
        return VoidElement(tag, *args, **kwargs)
    return Element(tag, *args, **kwargs)
