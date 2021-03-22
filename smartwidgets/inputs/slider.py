from typing import Union, Any, Callable

from dearpygui import core as dpg

from .bases import SmartInput, SmartObject, SmartDependant, ConfigProperty, _Slider


__all__ = [
    "SliderInt4",
    "SliderInt3",
    "SliderInt2",
    "SliderInt",
    "SliderFloat4",
    "SliderFloat3",
    "SliderFloat2",
    "SliderFloat",
]

# Aside from slightly different type-check, default
# values, and <cls._func>, 99% of this is copy/paste.
# Using **kwargs would mean that these wouldn't have 
# signatures of their own.


class SliderInt4(_Slider):
    _func = dpg.add_slider_int4

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[int] = [0, 0, 0, 0],
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d"
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )


class SliderInt3(_Slider):
    _func = dpg.add_slider_int3

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[int] = [0, 0, 0],
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d"
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )


class SliderInt2(_Slider):
    _func = dpg.add_slider_int2

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[int] = [0, 0],
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d"
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )


class SliderInt(_Slider):
    _func = dpg.add_slider_int

    height: int = ConfigProperty()
    vertical: bool = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: int = 0,
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d",
        height: int = 0,
        vertical: bool = False,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )

        self.height = height
        self.vertical = vertical


class SliderFloat4(_Slider):
    _func = dpg.add_slider_float4

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[float] = [0, 0, 0, 0],
        width: int = 0,
        min_value: float = 0.1, 
        max_value: float = 1.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d"
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )


class SliderFloat3(_Slider):
    _func = dpg.add_slider_float3

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[float] = [0, 0, 0],
        width: int = 0,
        min_value: float = 0.1, 
        max_value: float = 1.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d"
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )


class SliderFloat2(_Slider):
    _func = dpg.add_slider_float2

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[float] = [0, 0],
        width: int = 0,
        min_value: float = 0.1, 
        max_value: float = 1.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d"
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )


class SliderFloat(_Slider):
    _func = dpg.add_slider_float

    height: int = ConfigProperty()
    vertical: bool = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: float = 0.1,
        width: int = 0,
        min_value: float = 0.1, 
        max_value: float = 1.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = "", 
        show: bool = True,
        readonly: bool = False,
        format: str = "%d",
        height: int = 0,
        vertical: bool = False,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            format=format,
            )

        self.height = height
        self.vertical = vertical
