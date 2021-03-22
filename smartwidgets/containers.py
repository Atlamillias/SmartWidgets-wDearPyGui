from dearpygui.core import *
from typing import Any, Callable, Union
from .bases import SmartObject, ConfigProperty, SmartDependant


__all__ = [
    "Window",
    "Child",
    "Group",
    "MenuBar",
    "Menu",
    "TabBar",
    "Tab",
    "Group",
    "Popup",
    "Tooltip",
    "TreeNode",
    "ManagedColumns"
]

# With the exception of Window, all others inherrit from 
# SmartDependant ('parent', 'before', 'name/id', 'label')

# This module needs defaults added to params, not __init__ bodies

class Window(SmartObject):
    """
    Base class for window items. Windows are the most top-level items - they cannot
    have parents, and must be the parent of all other items either directly (i.e. a 
    button in a window) or indirectly (i.e. a button within a group that's within a 
    window).

    Parameters:
        label: The displayed name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass. Passing <" "> will effectively hide
        the label.

        *Optional Keyword-only Parameters

        id: A unique name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass.

        width: The items' horizontal size (in pixels).

        height: The items' vertical size (in pixels).

        x_pos, y_pos: The horizontal/vertical location on-screen for the top-left
        corner of the item (in pixels).

        autosize: If True, the items' width and height will automatically scale to its 
        children. This also disables and removes the lower-right drag handle.

        no_resize: If True, the items' lower-right drag handle will be disabled, 
        preventing it from being resized through the ui.

        no_title_bar: If True, the title bar is disabled for the item.

        no_move: If True, the item cannot be moved through the ui.

        no_scrollbar: If True, the item will have the vertical scrollbar hidden.
        This does not disable scrolling.

        horizontal_scrollbar: If True, the horizontal scrollbar is viewable. Scrolling
        is enabled regardless.

        no_collapse: If True, the item cannot be collapsed through the ui.

        collapsed:  If True, the item will be collapsed on creation (click the item
        to uncollapse through the ui).

        no_focus_on_appearing: If True, the item will not be focused when it is shown.

        no_bring_to_front_on_focus: If True, the item will not be brought into
        the foreground when it is focused.

        menubar: If True, the items' menubar will be disabled.

        no_close: If True, the items' close button in the top-right corner is removed,
        preventing the item from being closed through the ui. 

        no_background: If True, the item's background will be completely transparent.
        Title and menu bars remain unaffected.

        show: If False, the item will not be viewable.
    
    """
    _func = add_window
    _addl_config = ["on_close"]
    _other_options = []

    width = ConfigProperty()
    height = ConfigProperty()
    x_pos = ConfigProperty()
    y_pos = ConfigProperty()
    autosize = ConfigProperty()
    no_resize = ConfigProperty()
    no_title_bar = ConfigProperty()
    no_move = ConfigProperty()
    no_scrollbar = ConfigProperty()
    no_collapse = ConfigProperty()
    collapsed = ConfigProperty()
    horizontal_scrollbar = ConfigProperty()
    no_focus_on_appearing = ConfigProperty()
    no_bring_to_front_on_focus = ConfigProperty()
    menubar = ConfigProperty()
    no_close = ConfigProperty()
    no_background = ConfigProperty()
    label = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self,
        label: str  = None,
        *,
        id: str = None,
        width: int = None,
        height: int = None,
        x_pos: int = None,
        y_pos: int = None,
        autosize: bool = False,
        no_resize: bool = False,
        no_title_bar: bool = False,
        no_move: bool = False,
        no_scrollbar: bool = False,
        no_collapse: bool = False,
        collapsed: bool = False,
        horizontal_scrollbar: bool = False,
        no_focus_on_appearing: bool = False,
        no_bring_to_front_on_focus: bool = False,
        menubar: bool = False,
        no_close: bool = False,
        no_background: bool = False,
        show: bool = True,
        on_close: Callable = None,
    ):
        super().__init__(id, label)
        self.width = width or 50
        self.height = height or 50
        self.x_pos = x_pos if x_pos is not None else 0
        self.y_pos = y_pos if y_pos is not None else 0
        self.autosize = autosize
        self.no_resize = no_resize
        self.no_title_bar = no_title_bar
        self.no_move = no_move
        self.no_scrollbar = no_scrollbar
        self.no_collapse = no_collapse
        self.horizontal_scrollbar = horizontal_scrollbar
        self.collapsed = collapsed
        self.no_focus_on_appearing = no_focus_on_appearing
        self.no_bring_to_front_on_focus = no_bring_to_front_on_focus
        self.menubar = menubar
        self.no_close = no_close
        self.no_background = no_background
        self.show = show

        self._on_close= on_close

    @property
    def pos(self):
        config = get_item_configuration(self.id)
        return config["x_pos"], config["y_pos"]

    @property
    def on_close(self):
        return self._on_close

    def refresh(self):
        """Deletes the item from dearpygui, and creates
        a new item with an state identical to the previous one. 
        Item is otherwise left unchanged. If the item is a parent
        to other items, those items will be deleted and not restored."""
        x, y = self.pos
        delete_item(self.id)
        self.x_pos, self.y_pos = x, y
        return self.add()

    def start(self):
        """Starts dearpygui with <self> as the primary window."""
        start_dearpygui(primary_window=self.id)

    def stop(self):
        """Stops the application."""
        stop_dearpygui()


class Child(SmartDependant):
    """
    Base class for child items. They are containers that can hold other items.

    Parameters:

        *Optional Keyword-only Parameters

        id: A unique name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass.

        width: The items' horizontal size (in pixels).

        height: The items' vertical size (in pixels).

        menubar: If True, the items' menubar will be disabled. 

        border: If False, the item will not have visible borders.

        autosize_x: If True, the width of the item will scale to its childrens' width.

        autosize_y: If True, the height of the item will scale to its childrens' height.

        autosize: If True, <autosize_x> and <autosize_y> are set to <True>

        no_scrollbar: If True, the item will have the vertical scrollbar hidden.
        This does not disable scrolling.

        horizontal_scrollbar: If True, the horizontal scrollbar is viewable. Scrolling
        is enabled regardless.

        parent: The name of the parenting item. Setting this after the item is registered
        in dearpygui (<self.add>) will move the item to the end of the new parent's 
        (value) stack.

        before: The id/name of the item, or the <SmartDependant> item, that
        this item will be placed before in the parent's stack of items. Setting this 
        after the item is registered in dearpygui (<self.add>) will move the item before
        its new neighbor (value) within it's current parent, if possible.

        tip: If provided, a tooltip is shown with the provided value when the item
        is hovered over.

        show: If False, the item will not be viewable.
        
    """
    _func = add_child

    show = ConfigProperty()
    tip = ConfigProperty()
    width = ConfigProperty()
    height = ConfigProperty()
    border = ConfigProperty()
    autosize_x = ConfigProperty()
    autosize_y = ConfigProperty()
    no_scrollbar = ConfigProperty()
    horizontal_scrollbar = ConfigProperty()
    menubar = ConfigProperty()

    def __init__(
        self,
        *,
        id: str = None,
        show: bool = True,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        width: int = None,
        height: int = None,
        border: bool = True,
        autosize_x: bool = False,
        autosize_y: bool = False,
        no_scrollbar: bool = False,
        horizontal_scrollbar: bool = False,
        menubar: bool = False,
        autosize: bool = False,
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.show = show
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.height = height or 0
        self.border = border
        self.autosize_x = autosize_x
        self.autosize_y = autosize_y
        self.no_scrollbar = no_scrollbar
        self.horizontal_scrollbar = horizontal_scrollbar
        self.menubar = menubar

        if autosize:
            self.autosize_x = True
            self.autosize_y = True

    @property
    def autosize(self):
        if self.autosize_x and self.autosize_y:
            return True
        
        return False

    @autosize.setter
    def autosize(self, value: bool):
        if not value:
            self.autosize_x = False
            self.autosize_y = False
        
        self.autosize_x = True
        self.autosize_y = True


class Group(SmartDependant):
    """
    Base class for Group items. Groups are containers (like Child items) with limited
    features. They allow more control over the layout of the items they contain.

    Parameters:

        *Optional Keyword-only Parameters

        id: A unique name for the item. This should not be declared as an instance
        attribute as it is handled by the superclass.

        width: The items' horizontal size (in pixels). 

        horizontal: If True, child items' will be aligned side-by-side 'in-line' with
        each other.

        horizontal_spacing: The side-by-side distance (in pixels) between the items' 
        children.

        parent: The name of the parenting item. Setting this after the item is registered
        in dearpygui (<self.add>) will move the item to the end of the new parent's 
        (value) stack.

        before: The id/name of the item, or the <SmartDependant> item, that
        this item will be placed before in the parent's stack of items. Setting this 
        after the item is registered in dearpygui (<self.add>) will move the item before
        its new neighbor (value) within it's current parent, if possible.

        tip: If provided, a tooltip is shown with the provided value when the item
        is hovered over.

        show: If False, the item will not be viewable.

    """
    _func = add_group
    show = ConfigProperty()
    tip = ConfigProperty()
    
    width = ConfigProperty()
    horizontal = ConfigProperty()
    horizontal_spacing = ConfigProperty()

    def __init__(
        self,
        *,
        id: str = None,
        show: bool = True,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        width: int = None,
        horizontal: bool = False,
        horizontal_spacing: float = None
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.show = show
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.horizontal = horizontal
        self.horizontal_spacing = horizontal_spacing or -1.0


class MenuBar(SmartDependant):
    _func = add_menu_bar

    show = ConfigProperty()
    
    def __init__(
        self,
        id: str = None,   
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.show = show
        self.parent = parent or ""
        self.before = before or ""

    @property
    def height(self):
        return get_item_configuration(self.id)['height']


class Menu(SmartDependant):
    _func = add_menu
    label = ConfigProperty()
    show = ConfigProperty()
    
    enabled = ConfigProperty()

    def __init__(
        self,
        id: str = None,
        label: str  = None,
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        enabled: bool = True
    ):

        super().__init__(id, label, parent, before)

        self.show = show
        self.parent = parent or ""
        self.before = before or ""
        self.enabled = enabled


class TabBar(SmartDependant):
    _func = add_tab_bar

    reorderable = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    show = ConfigProperty()
    

    def __init__(
        self,
        id: str = None,
        reorderable: bool = False,
        callback: Callable = None,
        callback_data: Any = None,
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.reorderable = reorderable
        self.callback = callback
        self.callback_data = callback_data
        self.show = show
        self.parent = parent or ""
        self.before = before or ""


class Tab(SmartDependant):
    _func = add_tab

    closable = ConfigProperty()
    label = ConfigProperty()
    show = ConfigProperty()
    no_reorder = ConfigProperty()
    leading = ConfigProperty()
    trailing = ConfigProperty()
    no_tooltip = ConfigProperty()
    tip = ConfigProperty()
    
    def __init__(
        self,
        id: str = None,
        closable: bool = False,
        label: str  = None,
        show: bool = True,
        no_reorder: bool = False,
        leading: bool = False,
        trailing: bool = False,
        no_tooltip: bool = False,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.closable = closable
        self.show = show
        self.no_reorder = no_reorder
        self.leading = leading
        self.trailing = trailing
        self.no_tooltip = no_tooltip
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""


class Popup(SmartDependant):
    _func = add_popup
    _addl_config = ['popupparent']

    mousebutton = ConfigProperty()
    modal = ConfigProperty()
    width = ConfigProperty()
    height = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self,
        popupparent: Union[str, SmartObject],
        id: str = None,
        mousebutton: int = None,
        modal: bool = False,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        width: int = None,
        height: int = None,
        show: bool = True
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.popupparent = popupparent
        self.mousebutton = mousebutton or 1
        self.modal = modal
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.height = height or 0
        self.show = show

    @property
    def popupparent(self):
        return self.popupparent


class Tooltip(SmartDependant):
    _func = add_tooltip
    _addl_config = ['tipparent']

    show = ConfigProperty()

    def __init__(
        self,
        tipparent: Union[str, SmartObject],
        id: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        show: bool = True
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self._tipparent = tipparent
        self.parent = parent or ""
        self.show = show

    @property
    def tipparent(self):
        return self._tipparent


class TreeNode(SmartDependant):
    _func = add_tree_node

    show = ConfigProperty()
    tip = ConfigProperty()
    default_open = ConfigProperty()
    open_on_double_click = ConfigProperty()
    open_on_arrow = ConfigProperty()
    leaf = ConfigProperty()
    bullet = ConfigProperty()

    def __init__(
        self,
        id: str = None,
        label: str  = None,
        show: bool = True,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartDependant] = None,
        default_open: bool = False,
        open_on_double_click: bool = False,
        open_on_arrow: bool = False,
        leaf: bool = False,
        bullet: bool = False
    ):
        super().__init__(id, label, parent, before)
        
        self.show = show
        self.tip = tip or ""
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet


class ManagedColumns(SmartDependant):
    _func = add_managed_columns
    columns = ConfigProperty()
    border = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self,
        id: str = None,
        columns: int = None,
        border: bool = False,
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):
        super().__init__(id, label = None, parent = parent, before = before)
        self.columns = columns if columns is not None else 0
        self.border = border
        self.show = show
   