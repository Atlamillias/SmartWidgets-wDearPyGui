from dearpygui import core as dpg

from smartwidgets.containers import *
from smartwidgets.node import *
from smartwidgets.inputs import *
from smartwidgets.buttons import *


SMARTITEMS = {}  # {"item string name": SmartObject}


def smartitem(id: str):
    """Convenience function. Returns the smartitem object in 
    <SMARTITEMS> if it exists, returning <None> otherwise."""
    if id in SMARTITEMS:
        return SMARTITEMS[id]
    
    return None
