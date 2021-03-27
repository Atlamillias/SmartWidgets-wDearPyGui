from typing import Any

from dearpygui import core as dpg

__all__ = [
    "ValueStorageProxy"
]


class ValueStorageProxy:
    """Middle-man for DearPyGui's value storage system. Returns 
    a callable object that returns the stored value."""
    _keygen_counter = None
    _value = None

    def __init__(self, value: Any, key: str = None):
        self._key = key or self._keygen()
        self._value = value

        dpg.add_value(self.key, self._value)

    def __call__(self):
        return dpg.get_value(self.key)

    def __get__(self):
        return self.__call__

    def __set__(self, instance, value):
        dpg.set_value(self.key, value)

    def __repr__(self):
        return f"{self.__class__.__qualname__}"

    def __str__(self):
        return {self.key: self._value}

    @classmethod
    def _keygen(cls):
        """Generates an key for value storage."""
        if cls._keygen_counter is None:
            cls._keygen_counter = 0

        while dpg.does_item_exist(id := f'{cls.__name__}<{cls._keygen_counter}>'):
            cls._keygen_counter += 1

        return id

    @property
    def key(self):
        return self._key
