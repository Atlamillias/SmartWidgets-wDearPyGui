from typing import Any

from dearpygui import core as dpg

__all__ = [
    "ValueStorageProxy"
]


class ValueStorageProxy:
    """Middle-man for DearPyGui's value storage system."""
    _keygen_counter = None
    _key = None
    _value = None

    def __init__(self, value: Any, key: str = None):
        self._key = key or self._keygen()
        self._value = value

        dpg.add_value(self._key, self._value)

    def __repr__(self):
        return f"{self.__class__.__qualname__}"

    def __str__(self):
        return str({self.key: self.value})

    @classmethod
    def _keygen(cls):
        """Generates an key for value storage."""
        if cls._keygen_counter is None:
            cls._keygen_counter = 0

        while dpg.get_value(key := f'{cls.__name__}<{cls._keygen_counter}>') is None:
            cls._keygen_counter += 1

        return key

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        self._value = dpg.get_value(self._key)
        return self._value

    @value.setter
    def value(self, value):
        dpg.set_value(self._key, value)

    def get(self):
        return self.value

    def set(self, value):
        dpg.set_value(self._key, value)
