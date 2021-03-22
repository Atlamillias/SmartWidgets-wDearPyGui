from typing import Callable, Any, Union

from ..bases import SmartObject, ConfigProperty, SmartDependant


class SmartInput(SmartDependant):
    _common_config = ["before", "parent", "default_value"]

    def __init__(
        self,
        *,
        # superclass/dearpygui args
        id: str = None, 
        label: str = None, 
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        ):

        super().__init__(id, label, parent=parent, before=before)
    
    def __enter__(self):  # overloaded
        # context manager isn't needed for non-parenting widgets, and
        # could be confusing
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):  # overloaded
        pass

    @property
    def default_value(self):
        return self._default_value


class _Input(SmartInput):
    min_clamped = ConfigProperty()
    max_clamped = ConfigProperty()
    width = ConfigProperty()
    on_enter = ConfigProperty()
    readonly = ConfigProperty()
    min_value = ConfigProperty()
    max_value = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    source = ConfigProperty()
    enabled = ConfigProperty()
    tip = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = None,
        label: str = None, 
        parent: Union[str, SmartObject] = None, 
        before: Union[str, SmartDependant] = None, 
        default_value = None,
        min_value = None, 
        max_value = None, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        width: int = None,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before, 
            )

        self.width = width
        self.min_value = min_value
        self.max_value = max_value
        self.max_clamped = max_clamped
        self.min_clamped = min_clamped
        self.callback = callback
        self.callback_data = callback_data
        self.source = source
        self.enabled = enabled
        self.on_enter = on_enter
        self.tip = tip
        self.show = show
        self.readonly = readonly
        self._default_value = default_value


class _Slider(SmartInput):
    format = ConfigProperty()
    width = ConfigProperty()
    no_input = ConfigProperty()
    clamped = ConfigProperty()
    min_value = ConfigProperty()
    max_value = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    source = ConfigProperty()
    enabled = ConfigProperty()
    tip = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self, 
        *, 
        id: str = None, 
        label: str = None, 
        parent: Union[str, SmartObject] = None, 
        before: Union[str, SmartDependant] = None, 
        default_value = None,
        min_value = None,
        max_value = None,
        width: int = None,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = None,
        tip: str = None,
        show: bool = True,
        format: str = None
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            )

        self._default_value = default_value
        self.width = width
        self.min_value = min_value
        self.max_value = max_value
        self.callback = callback
        self.callback_data = callback_data
        self.no_input = no_input
        self.clamped = clamped
        self.source = source
        self.enabled = enabled
        self.tip = tip
        self.show = show
        self.format = format


class _Drag(_Slider):  # 1 argument difference between drag and slider items
    speed = ConfigProperty()

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = None, 
        parent: Union[str, SmartObject] = None, 
        before: Union[str, SmartDependant] = None,
        default_value = None,
        speed = None, 
        min_value = None,
        max_value = None,
        width: int = None,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = None,
        tip: str = None,
        show: bool = True,
        format: str = None
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

        self.speed = speed
