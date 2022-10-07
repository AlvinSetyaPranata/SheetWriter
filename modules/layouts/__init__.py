from tkinter import (
    BOTH, CENTER, LEFT, Label, Frame, StringVar, LabelFrame, Entry, DISABLED, X, NORMAL
)
from tkinter.ttk import (
    Button
)

class BaseLayout:
    def __init__(self):
        self._rendered = False


    def _prepare_obj(self):
        # this method should not be called outside function and called after render function get called
        pass

    def render(self):
        # this method should be overwritten
        pass
        