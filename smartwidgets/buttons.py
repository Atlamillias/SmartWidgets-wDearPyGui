from .bases import SmartDependant, ConfigProperty
from typing import Union, Callable, Any
from dearpygui import core as dpg


class Button(SmartDependant):
    _func = dpg.add_button

    small = ConfigProperty()
    arrow = ConfigProperty()
    direction = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    tip = ConfigProperty()
    width = ConfigProperty()
    height = ConfigProperty()
    label = ConfigProperty()
    show = ConfigProperty()
    enabled = ConfigProperty()

    def __init__(
        self, 
        id: str = None, 
        label: str = None,

        small: bool = False,
        arrow: bool = False,
        direction: int = None,
        callback: Callable = None,
        callback_data: Any = None,
        tip: str = None,
        parent: str = None,
        before: str = None,
        width: int = None,
        height: int = None,
        show: bool = True,
        enabled: bool = True,
        ):
        super().__init__(id, label, parent, before)
        self.small = small
        self.arrow = arrow  
        self.direction = direction or 0
        self.callback = callback
        self.callback_data = callback_data
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 100
        self.height = height or 50
        self.show = show
        self.enabled = enabled

    def __enter__(self):  # overloaded
        # context manager isn't needed for non-parenting widgets
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
