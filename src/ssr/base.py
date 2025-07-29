from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Union


class Buildable(ABC):
    @abstractmethod
    def __build__(self) -> str:
        pass

    def render(self) -> str:
        return self.__build__()


class Text(Buildable):
    def __init__(self, value: str) -> None:
        self._value = value

    def __build__(self) -> str:
        return self._value


class Node(Buildable):
    def __init__(
        self,
        *,
        class_: Optional[str] = None,
        id: Optional[str] = None,
        data: Optional[Dict[str, str]] = None,
        style: Optional[Dict[str, str]] = None,
        aria: Optional[Dict[str, str]] = None,
        disabled: bool = False,
        children: Optional[List[Union["Node", "Text", str]]] = None,
        **kwargs,
    ) -> None:
        self._class = class_
        self._id = id
        self._data = data or {}
        self._style = style or {}
        self._aria = aria or {}
        self._disabled = disabled
        self._kwargs = kwargs

        processed_children = []
        if children:
            for child in children:
                if isinstance(child, str):
                    processed_children.append(Text(child))
                else:
                    processed_children.append(child)
        self._children = processed_children

    def _render_attrs(self) -> str:
        attrs = []
        if self._class:
            attrs.append(f'class="{self._class}"')
        if self._id:
            attrs.append(f'id="{self._id}"')
        if self._style:
            style_str = "; ".join(f"{key}: {value}" for key, value in self._style.items())
            attrs.append(f'style="{style_str}"')
        if self._disabled:
            attrs.append("disabled")
        for key, value in self._data.items():
            attrs.append(f'data-{key}="{value}"')
        for key, value in self._aria.items():
            attrs.append(f'aria-{key}="{value}"')
        for key, value in self._kwargs.items():
            if value is not None:
                attr_name = key.replace("_", "") if key.startswith("on_") else key.replace("_", "-")
                attrs.append(f'{attr_name}="{value}"')
        return " ".join(attrs)

    def __build__(self) -> str:
        raise NotImplementedError()


class Element(Node):
    def __init__(self, tag: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._tag = tag

    def __build__(self) -> str:
        children_str = "".join(child.__build__() for child in self._children)
        return f"<{self._tag} {self._render_attrs()}>{children_str}</{self._tag}>"


class VoidElement(Node):
    def __init__(self, tag: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._tag = tag

    def __build__(self) -> str:
        return f"<{self._tag} {self._render_attrs()} />"
