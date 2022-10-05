from tkinter import (
    BOTH, CENTER, LEFT, Label, Frame, Button, Entry, OptionMenu, StringVar, LabelFrame
)


class BaseLayout:
    def __init__(self, **handlers):

        try:
            self.handlers = handlers

        except KeyError:
            pass

        self._rendered = False


    @property
    def assign_handler(self):
        if not self.handlers:
            raise ValueError("No such handlers are defined!")


        for widget in self.handlers:
            widget.bind(self.handlers[widget][0], self.handlers[widget][1])


    def render(self):
        # this method should be overwritten
        pass
        