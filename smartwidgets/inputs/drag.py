from typing import Union, Any, Callable

from dearpygui import core as dpg

from .bases import SmartObject, SmartDependant, _Drag


__all__ = [
    "DragInt4",
    "DragInt3",
    "DragInt2",
    "DragInt",
    "DragFloat4",
    "DragFloat3",
    "DragFloat2",
    "DragFloat",
]

# Aside from slightly different type-check, default
# values, and <cls._func>, 99% of this is copy/paste.
# Using **kwargs would mean that these wouldn't have 
# signatures of their own.

class DragInt4(_Drag):
    _func = dpg.add_drag_int4

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: list[int] = [0, 0, 0, 0],
        speed: float = 1.0, 
        min_value: int = 0,
        max_value: int = 100,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%d'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragInt3(_Drag):
    _func = dpg.add_drag_int3

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: list[int] = [0, 0, 0],
        speed: float = 1.0, 
        min_value: int = 0,
        max_value: int = 100,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%d'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragInt2(_Drag):
    _func = dpg.add_drag_int2

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: list[int] = [0, 0],
        speed: float = 1.0, 
        min_value: int = 0,
        max_value: int = 100,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%d'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragInt(_Drag):
    _func = dpg.add_drag_int

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: int = 0,
        speed: float = 1.0, 
        min_value: int = 0,
        max_value: int = 100,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%d'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragFloat4(_Drag):
    _func = dpg.add_drag_float4

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        speed: float = 1.0, 
        min_value: float = 0.1,
        max_value: float = 1.0,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%0.3f'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragFloat3(_Drag):
    _func = dpg.add_drag_float3

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: list[float] = [0.0, 0.0, 0.0],
        speed: float = 1.0, 
        min_value: float = 0.1,
        max_value: float = 1.0,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%0.3f'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragFloat2(_Drag):
    _func = dpg.add_drag_float2

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: list[float] = [0.0, 0.0],
        speed: float = 1.0, 
        min_value: float = 0.1,
        max_value: float = 1.0,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%0.3f'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )


class DragFloat(_Drag):
    _func = dpg.add_drag_float

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value: float = 0.0,
        speed: float = 1.0, 
        min_value: float = 0.1,
        max_value: float = 1.0,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = "",
        show: bool = True,
        format: str = '%0.3f'
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            format=format,
            )
