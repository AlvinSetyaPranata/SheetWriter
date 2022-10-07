from . import *


class Table:
    def __init__(self, parent, header_data, fill_parent=False, onSelect=None):
        """
        :header_data => contains all data in header
        """
        
        self.header_data = header_data
        self.fill_parent = fill_parent
        self.parent = parent
        
        self._bodies = []
        self._headers = []

        
        self.container = Frame(self.parent)
        self.scroll_upper_container = Frame(self.container)
        self.table = Treeview(self.scroll_upper_container, columns=self.header_data, show="headings", selectmode="browse")
        self.scroll_y = Scrollbar(self.scroll_upper_container, orient=VERTICAL, command=self.table.yview)
        self.scroll_x = Scrollbar(self.container, orient=HORIZONTAL, command=self.table.xview)

        self.table.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.table.bind("<<TreeviewSelect>>", onSelect)


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


    def add_row(self, data):
        """
        if length :data is not equal to header data then the empty cell will be created with empty string by default

        """

        if len(data[0]) > len(self.header_data):
            raise ValueError("Length of row out of header range!")


        for row in data:
            self.table.insert('', END, values=row)
        
        if self._rendered:
            self.render()
    
