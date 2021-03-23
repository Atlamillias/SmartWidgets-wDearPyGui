from .bases import SmartDependant, ConfigProperty
from typing import Any, Callable
import dearpygui.core as dpg


__all__ = [
    "NodeEditor",
    "Node",
    "NodeAttribute"
]


class NodeEditor(SmartDependant):
    _func = dpg.add_node_editor
    _addl_config = ['before', 'link_callback', 'delink_callback']

    show = ConfigProperty()
    
    delink_callback = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *,
        show: bool = True,
        parent: str = "",
        before: str = "",
        link_callback: Callable = None,
        delink_callback: Callable = None
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.show = show
        self._link_callback = link_callback
        self._delink_callback = delink_callback

    @property
    def link_callback(self):
        return self._link_callback

    @property
    def delink_callback(self):
        return self._delink_callback


class Node(SmartDependant):
    _func = dpg.add_node

    show: bool = ConfigProperty()
    draggable: bool = ConfigProperty()
    x_pos: int = ConfigProperty()
    y_pos: int = ConfigProperty()

    def __init__(
        self,
        id: str = None,
        *,
        label: str  = "",
        show: bool = True,
        draggable: bool = True,
        parent: str = "",
        before: str = "",
        x_pos: int = None,
        y_pos: int = None,
        ):
        super().__init__(id, label, parent, before)
        self.show = show
        self.draggable = draggable
        self.x_pos = x_pos
        self.y_pos = y_pos


class NodeAttribute(SmartDependant):
    _func = dpg.add_node_attribute
    
    show = ConfigProperty()
    output = ConfigProperty()
    static = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        show: bool = True,
        parent: str = "",
        before: str = "",
        output: bool = False,
        static: bool = False
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.show = show
        self.output = output
        self.static = static
