from typing import Any, Callable, ClassVar, Iterator, Optional, Type, TypeVar

from screen.drawing import Color
from screen.primitives import HorizontalAlignment
from screen.primitives import Thickness
from screen.primitives import VerticalAlignment


C = TypeVar("C", bound=Control)


def option(name: str, type: Type[Any], default: Optional[Any], optional: bool, remeasure: bool) -> Callable[[Type[C]], Type[C]]: ...

class Control:
    default_background: ClassVar[Optional[Color]]
    default_foreground: ClassVar[Optional[Color]]
    default_height: ClassVar[Optional[int]]
    default_horizontal_alignment: ClassVar[Optional[HorizontalAlignment]]
    default_margin: ClassVar[Optional[Thickness]]
    default_max_height: ClassVar[Optional[int]]
    default_max_width: ClassVar[Optional[int]]
    default_min_height: ClassVar[Optional[int]]
    default_min_width: ClassVar[Optional[int]]
    default_padding: ClassVar[Optional[Thickness]]
    default_vertical_alignment: ClassVar[Optional[VerticalAlignment]]
    default_width: ClassVar[Optional[int]]

    def __init__(
        self,
        *,
        background: Color=...,
        foreground: Color=...,
        height: int=...,
        horizontal_alignment: HorizontalAlignment=...,
        margin: Thickness=...,
        max_height: int=...,
        max_width: int=...,
        min_height: int=...,
        min_width: int=...,
        padding: Thickness=...,
        vertical_alignment: VerticalAlignment=...,
        width: int=...,
    ) -> None: ...

    @property
    def background(self) -> Optional[Color]: ...
    @background.setter
    def background(self, value: Optional[Color]): ...
    @property
    def foreground(self) -> Optional[Color]: ...
    @foreground.setter
    def foreground(self, value: Optional[Color]): ...
    @property
    def height(self) -> Optional[int]: ...
    @height.setter
    def height(self, value: Optional[int]): ...
    @property
    def horizontal_alignment(self) -> HorizontalAlignment: ...
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: Optional[HorizontalAlignment]): ...
    @property
    def margin(self) -> Thickness: ...
    @margin.setter
    def margin(self, value: Optional[Thickness]): ...
    @property
    def max_height(self) -> int: ...
    @max_height.setter
    def max_height(self, value: Optional[int]): ...
    @property
    def max_width(self) -> int: ...
    @max_width.setter
    def max_width(self, value: Optional[int]): ...
    @property
    def min_height(self) -> int: ...
    @min_height.setter
    def min_height(self, value: Optional[int]): ...
    @property
    def min_width(self) -> int: ...
    @min_width.setter
    def min_width(self, value: Optional[int]): ...
    @property
    def padding(self) -> Thickness: ...
    @padding.setter
    def padding(self, value: Optional[Thickness]): ...
    @property
    def vertical_alignment(self) -> VerticalAlignment: ...
    @vertical_alignment.setter
    def vertical_alignment(self, value: Optional[VerticalAlignment]): ...
    @property
    def width(self) -> Optional[int]: ...
    @width.setter
    def width(self, value: Optional[int]): ...

    def measure(self, h: int, w: int, **kwargs) -> tuple[int, int]: ...
    def measure_core(self, h: int, w: int, **kwargs) -> tuple[int, int]: ...
    def render(self, h: int, w: int, **kwargs) -> Iterator[str]: ...
