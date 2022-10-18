from autocomplete import AutoSearch


class Validation:

    @classmethod
    def unbind_widget(cls, widget):
        widget.configure(bg="white", fg="black")
        widget.unbind("<Button-1>")


    @classmethod
    def type_validation(cls, widgets, *types):
        mistakes = []
        
        for i in range(len(widgets)):
            if type(widgets[i].get()) != types[i]:
                mistakes.append(widgets[i])

        cls.check(mistakes)

    @classmethod
    def value_validation(cls, widgets, data):
        mistakes = []

        for i in range(len(widgets)):
            if not widgets[i].value in data:
                mistakes.append(widgets[i])

        cls.check(mistakes)

    def check(self, mistakes):
        """
        Called after validation function
        """

        for widget in mistakes:
            widget.configure(bg="red", fg="white")
            widget.bind("<Button-1>", lambda e: self.unbind_widget(widget))
