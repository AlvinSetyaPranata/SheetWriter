from . import *


class Table:
    def __init__(self, parent, header_data, fill_parent=False, onSelect=None, mode="browse"):
        """
        :header_data => contains all data in header
        """
        
        self.header_data = header_data
        self.fill_parent = fill_parent
        self.parent = parent
        # self.handle_change = onChange
        
        self._bodies = []
        self._headers = []

        
        self.container = Frame(self.parent)
        self.scroll_upper_container = Frame(self.container)
        self.table = Treeview(self.scroll_upper_container, columns=self.header_data, show="headings", selectmode=mode)
        self.scroll_y = Scrollbar(self.scroll_upper_container, orient=VERTICAL, command=self.table.yview)
        self.scroll_x = Scrollbar(self.container, orient=HORIZONTAL, command=self.table.xview)

        self.table.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.table.bind("<<TreeviewSelect>>", lambda event: onSelect(self.table))

        for col in self.table["columns"]:
            self.table.column(col, anchor=CENTER, width=118)

        self._rendered = False

        
    def render(self):
        self._header_init()

        # render container
        self.container.pack(expand=self.fill_parent, side=TOP, pady=10)
        self.scroll_upper_container.pack()
        self.table.pack(expand=False, side=LEFT)
        self.scroll_y.pack(fill=Y, expand=True, side=LEFT, padx=2)
        self.scroll_x.pack(fill=X, expand=True, pady=2)


        self._rendered = True


    def _header_init(self):
        for header in self.header_data:
            self.table.heading(header, text=header, anchor=CENTER)


    @classmethod
    def fill_null(cls, list_, length):
        for _ in range(len(list_) - length):
            list_.append("")

        return list_


    def add_row(self, *data):
        """
        if length :data is less than length of header data then the empty cell will be created with empty string by default

        """

        _header_length = len(self.header_data)
        

        for row in data:
            if len(row) > _header_length:
                raise ValueError("Length of row out of header range!")


            elif len(row) < _header_length:
                row = self.fill_null(row, _header_length)

            self._bodies.append(row)
            self.table.insert('', END, values=row)

