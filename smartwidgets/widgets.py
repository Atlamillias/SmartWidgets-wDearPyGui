from typing import Union, Callable, Any

from dearpygui import core as dpg

from .bases import SmartObject, SmartDependant, ConfigProperty, AddOnlyMixin


__all__ = [
    "Text"
]


class Text(SmartDependant, AddOnlyMixin):
    _func = dpg.add_text
    _addl_config = ["parent", "before", "default_value"]

    wrap = ConfigProperty()
    color = ConfigProperty()  #rgba
    bullet = ConfigProperty()
    tip = ConfigProperty()
    source = ConfigProperty()
    default_value = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self,
        default_value: str = True,
        *,
        id: Union[str, None] = None,
        parent: Union[str, SmartObject, None] = "",
        before: Union[str, SmartDependant, None] = "",
        wrap: int = -1,
        color: list[float] = [255.0, 255.0, 255.0, 255.0],
        bullet: bool = False,
        tip: str = "",
        source: str = "",
        show: bool = True,

    ):
        super().__init__(
            id=id,
            label=None,
            parent=parent,
            before=before
        )

        self._default_value = default_value
        self.wrap = wrap
        self.color = color
        self.bullet = bullet
        self.tip = tip
        self.source = source
        self.show = show

    @property
    def default_value(self):
        return self._default_value
