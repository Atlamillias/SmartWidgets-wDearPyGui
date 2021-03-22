from __future__ import annotations
from typing import Union, Callable

from dearpygui.core import *

from smartwidgets import smartitem, SMARTITEMS


__all__ = [
    "SMARTITEMS",
    "smartitem",
    "ConfigProperty",
    "SmartObject",
    "SmartDependant",
]


# these cannot be changed via core.configure_item
# or fetched with core.get_item_configuration
# so they require specific handling
# and are common enough to warrant a constant
SPECIAL_CONFIG = {
    # option: (getter, (setter, {**kwargs}))
    # getters so far only have required 1 argument (item name/id)
    'callback': (get_item_callback, (set_item_callback, {
        "item": "id",
        "callback": "callback",
        "callback_data": "callback_data"
    })),
    'callback_data': (get_item_callback_data, (set_item_callback_data, {
        "item": "id",
        "callback_data": "callback_data"
    })),
}


class ConfigProperty:
    """Descriptor for general smartwidget configs. Retrieves and
    updates properties dearpygui. Used for the *required* arguments."""

    def __set_name__(self, owner, name):
        self.name = name
        self.owner = owner

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        value = None
        if instance.is_valid:  # exists in dpg
            # updates from dearpygui first since it may have
            # been changed externally
            # for this reason, __dict__ needs to be used
            # instead of __set/getitem__
            if self.name in SPECIAL_CONFIG:
                value = SPECIAL_CONFIG[self.name][0](instance.id)
            else:
                value = get_item_configuration(instance.id)[self.name]

            instance.__dict__[self.name] = value
        else:
            value = instance.__dict__[self.name]

        return value

    def __set__(self, instance, value):
        # can pass SmartObject instead of SmartObject.id
        # as arguments for other SmartObjects (i.e. parent, before, etc.)
        if isinstance(value, SmartObject):
            value = value.id

        instance.__dict__[self.name] = value

        # dearpygui config
        if instance.is_valid:  # exists in dpg
            if self.name in SPECIAL_CONFIG:
                setter, kwargs = SPECIAL_CONFIG[self.name][1]
                for arg, val in kwargs.copy().items():
                    kwargs[arg] = instance.__dict__[val]

                setter(**kwargs)
            else:
                configure_item(instance.id, **{self.name: value})

    def __delete__(self, instance):
        del self
    

class _SmartObject:
    """
    Low-level base class for SmartObject classes.

    Class variables:
        _func: Function called to add widget  in dearpgyui i.e. 
        core.add_window, core.add_button, etc. High-level subclasses 
        that create items need to overload this.

        _generator_id: Used as reference for generating item id's 
        if one isn't provided.

        _options: Cache for <cls.options> - populated on first 
        instance using <_other_options> and <_addl_config>.

        _option_desc: Descriptors used to identify which attrs are 
        "config" attrs. Attributes using these descriptors will be
        sent to dearpygui as config options for item setup.

        _addl_config: Contains "config" attributes that don't use a 
        custom descriptor, but are necessary for dearpygui item
        setup. These are either defined on <_SmartObject> subclasses 
        as properties (because they require unique functionality), or 
        are only used for initial widget setup and are more 'private'. 
        Attributes here will probably be fairly unique to the item.

        _common_config: Same as <_addl_config>. Stores configuration 
        attributes that will be most common between items. 
        Mid-level-subclasses will probably overload this. Remember to
        nclude the inherited classes' <_common_config> if overloaded.


    The purpose of this class is to set up and build the Python 
    representation of a dearpygui item, as well as the item in dearpygui 
    itself. It is not supposed to be instantiated directly - only 
    subclassed. Arguments that are specified in <_common_config>, 
    <_addl_config>, or are declared as class properties using a descriptor 
    class in <_option_desc>, are passed to <_func>. 

    """

    _func: Callable = None  
    _generator_id: int = None

    _options: list[str] = None
    _option_desc: list = [ConfigProperty]
    _addl_config: list[str] = []  # internally expects an iterable so not None
    _common_config: list[str] = []  # internally expects an iterable so not None

    def __init__(self, id: Union[str, None] = None, label: Union[str, None] = None):
        self.id = id if id is not None else self._make_id()
        self.label = self.id if label is None else label

        SMARTITEMS[self.id] = self

    def __getitem__(self, key):
        return self[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __enter__(self):
        return self.add()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end()

    def __str__(self):
        return f"{self.id}"

    def __repr__(self):
        try:
            return f'<{self.__class__.__name__}({self.id})>'
        except AttributeError:
            self.id = self._make_id()
            return f'<{self.__class__.__name__}({self.id})>'

    @classmethod
    def _make_id(cls):
        """Generates an item's id if one was not provided on initialization."""
        if cls._generator_id is None:
            cls._generator_id = 0

        while does_item_exist(id := f'{cls.__name__}<{cls._generator_id}>'):
            cls._generator_id += 1

        return id

    @classmethod
    def options(cls):
        """
        Returns a list of the options used by dearpygui for item setup. 
        Most of them can be changed after the item has been added.
        """
        # cache
        if not cls._options:
            cls._options = [
                optn for optn, value in cls.__dict__.items()
                if type(value) in cls._option_desc
                ]

            [
                cls._options.append(optn) for optn in 
                [*cls._addl_config, *cls._common_config]
            ]

        return cls._options

    @property
    def is_valid(self):
        """Checks if the item exists in dearpygui."""
        # used by ConfigProperty to properly update
        # values in dearpygui if necessary
        return does_item_exist(self.id)

    def add(self):
        """Adds the item to dearpygui. Behaves exactly like dearpygui.core.add_*.
         Needs to be followed by <self.end> if this is called directly."""
        self._func(name=self.id, **self.configuration())
        return self

    @staticmethod
    def end():
        """Ends the items' stack. Behaves exactly like <dearpygui.core.end>.
         If the item is a parent item (an item that can hold children), this 
        must be used after <self.add> before adding a new parent stack."""
        return end()

    def configuration(self):
        """Returns a dictionary of the items' configuration 
        options and their current values."""
        return {
            prop: getattr(self, prop) for prop in self.options()
        }


class SmartObject(_SmartObject):
    """
    Base class for top-level widgets, or child widget subclasses.

    Parameters:
    
        id: A unique name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass.

        label: The displayed name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass. Passing <" "> will effectively hide
        the label.
    """

    def __init__(self, id: Union[str, None], label: Union[str, None]):
        super().__init__(id, label)

    def children(self):
        """Returns a list of the items children."""
        return get_item_children(self.id)

    def is_activated(self):
        """Checks the items' status."""
        return is_item_activated(self.id)

    def is_container(self):
        """Checks if the item is a container."""
        return is_item_container(self.id)

    def is_focused(self):
        """Checks if the item is currently focused."""
        return is_item_focused(self.id)

    def is_hovered(self):
        """Checks if the item is currently hovered."""
        return is_item_hovered(self.id)

    def is_visible(self):
        """Checks if the item is currently visible on screen."""
        return is_item_visible(self.id)
    
    def was_clicked(self):
        # needs docstring
        # is/was clicked?
        # vague function name from dpg
        # need to confirm functionality
        return is_item_clicked(self.id)

    def was_edited(self):
        # needs docstring
        # is/was edited?
        # vague function name from dpg
        # need to confirm functionality
        return is_item_edited(self.id)

    def delete(self):  # better alternative to overloading __del__
        """Unregisters the item in dearpygui and destroys the item."""
        delete_item(self.id)

        try:
            SMARTITEMS.pop(self.id)
        finally:
            del self


class SmartDependant(SmartObject):
    """
    Base class for most dearpygui widgets. SmartDependant items require a 
    parent.

    Parameters:
        id: A unique name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass.

        label: The displayed name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass. Passing <" "> will effectively hide
        the label.

        parent: The name of the parenting item. Setting this after the item is registered
        in dearpygui (<self.add>) will move the item to the new parent (value)
        if possible.

        before: The id/name of the item, or the <SmartDependant> item, that
        this item will be placed before in the parent's stack of items. Setting this 
        after the item is registered in dearpygui (<self.add>) will move the item near its
        new neighbor (value) within it's current parent, if possible.
    """
    _common_config = ["before", "parent"]

    def __init__(
        self, 
        id: Union[str, None],
        label: Union[str, None],
        parent: Union[str, SmartObject, None],
        before: Union[str, SmartDependant, None],
        ):
        super().__init__(id=id, label=label)
        self._parent = parent or ""
        self._before = before or ""

    @property
    def parent(self):
        if self.is_valid:
            # should have a parent once item is added to dpg
            # otherwise it can't exist
            self._parent = get_item_parent(self.id)

        return str(self._parent)

    @parent.setter
    def parent(self, value: Union[str, SmartObject]):
        value = str(value)
        if self.is_valid:
            self.move(parent=value, before="")
     
        self._parent = value

    @property
    def before(self):
        if self.is_valid:
            # may not be accurate
            pass

        return self._before

    @before.setter
    def before(self, value: Union[str, SmartDependant]):
        value = str(value)
        if self.is_valid:
            self.move(parent=self.parent, before=value)

        self._before = str(value)
    
    def delete(self):  # overloaded - needs to remove children from SMARTITEMS
        """Unregisters the item in dearpygui and destroys the item, and its children."""
        childs = self.children()

        if childs:
            for child in childs:
                if (sitem := smartitem(child)):
                    sitem.delete()

        try:
            SMARTITEMS.pop(self.id)
        finally:
            delete_item(self.id)

        try:
            del self
        finally:
            pass

    def move(self, parent: str | SmartObject, before: str | SmartDependant = None):
        """Changes the items parent, moving it to the end of the new parents' stack."""
        move_item(self.id, parent= str(parent), before = str(before) or "")

    def move_up(self):
        """Moves the item up 1 in the parents' stack."""
        move_item_up(self.id)

    def move_down(self):
        """Moves the item down 1 in the parents' stack."""
        move_item_down(self.id)
