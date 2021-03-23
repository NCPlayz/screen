from screen.controls import Control, property
from screen.controls.primitives import Placement


class Popup(Control):
    """
    Represents the base class for a pop-up control.
    """

    # fmt: off
    horizontal_offset = property(int,       0,                True, False, False)
    placement         = property(Placement, Placement.cursor, True, False, False)
    vertical_offset   = property(int,       0,                True, False, False)
    # fmt: on


__all__ = [
    "Popup",
]
