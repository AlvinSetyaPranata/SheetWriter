from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showinfo, showerror, showwarning
from . import *
from modules.components.table import Table
from PIL import Image, ImageTk
from modules.utils.writer import Writer
from modules.handler.autocomplete import AutoSearch
from modules.utils.reader import XlsSupport


class ChangesLayout(BaseLayout):
    def __init__(self, parent, get_src_func, f_handler, loader):
        super().__init__()

        self.parent = parent
        self.main_frame = Frame(self.parent)
        self.row_id = []
        self.detached_items = set()
        self.data_obj = []
        self.src_file_func = get_src_func
        self.f_handler = f_handler
        self.loader = loader

        self.item_counter_vars = StringVar()
        self.item_counter_vars.set("Jumlah barang terinput: 0")
        self.item_counter = 0

        self.table = Table(self.main_frame, ("Kode Barang", "Nama Barang", "Bulan", "Tahun", "Kuantitas"), onSelect=self.handle_select, mode="extended")

    def load_images(self):
        _undo_image = Image.open("assets/undo.png")
        _delete_image = Image.open("assets/delete.png")
        _export_image = Image.open("assets/export.png")

        _undo_image = _undo_image.resize((20, 20), Image.ANTIALIAS)
        _delete_image = _delete_image.resize((20, 20), Image.ANTIALIAS)
        _export_image = _export_image.resize((20, 20), Image.ANTIALIAS)

        self._undo_image = ImageTk.PhotoImage(_undo_image)
        self._delete_image = ImageTk.PhotoImage(_delete_image)
        self._export_image = ImageTk.PhotoImage(_export_image)


    def handle_delete(self, table, *items):
        # create handler for delete an item
        for item in items:
            table.detach(item)
            self.detached_items.add(item)
            self.update_counter(-1)

        self.remove_btn.configure(state=DISABLED)
        self.undo_btn.configure(state=NORMAL)

        self.check_table()
        

    def load_(self):
        file = askopenfilename()

        if not file:
            return

        
        self.table.add_row(self.loader.load(file))


    def update_counter(self, total):
        """
        if want to decrase by one then pass :total as negative value, and vice verca
        """
        
        self.item_counter = self.item_counter + total

        self.item_counter_vars.set(f"Total barang terinput: {self.item_counter}")
        

    def handle_undo(self, table):
        for item in self.detached_items:
            table.move(item, '', 0)
            self.update_counter(1)

        self.detached_items.clear()
        self.undo_btn.configure(state=DISABLED)

        self.check_table()

    def handle_add(self, autosearch, data):
        self.table.add_row(data)

        self.data_obj.append(
            (autosearch.search_by_code(data[0]), autosearch.search_months(data[2]))
        )

        self.update_counter(1)

        self.check_table()


    def check_table(self):
        if not self.table._bodies:
            self.export_btn.configure(state=DISABLED)
            return


        self.export_btn.configure(state=NORMAL)

    def alert(self, type_, msg):
        if type_ == "error":
            showerror("Error", msg)
        elif type_ == "info":
            showinfo("Info", msg)
        elif type_ == "warning":
            showwarning("Warning", msg)


    def _export(self):
        _ftarget = asksaveasfilename(filetypes=(("Excel 2003 format", ".xls"), ("Excel 2007 format", ".xlsx")))

        if not _ftarget:
            return

        if not "." in _ftarget:
            _ftarget += ".xls"  # default extension if file format is not specified


        w  = Writer(_ftarget, self.src_file_func())
        search = AutoSearch(self.f_handler, self.alert)

        search.load_data()


        for row in self.table.table.get_children():
            code, _, month, year, value = self.table.table.item(row)["values"]
            # print(search.find_code_obj(str(code)))

            row_code, _ = XlsSupport.split_coord(search.find_code_obj(str(code))[0].coordinate)
            _, col_month = XlsSupport.split_coord(search.find_month_coord(str(year), str(month))[0].coordinate)

            w.modify("".join((col_month, row_code)), value)

        w.save()

        # Cleaning the table

        for row in self.table.table.get_children():
            self.table.table.delete(row)

        for item in self.detached_items:
            self.table.table.delete(item)

        showinfo("Info", f"File sudah terekspor di {_ftarget}!")

    def handle_select(self, table):
        items = table.selection()

        if items:
            self.remove_btn.configure(state=NORMAL)

        else:
            self.remove_btn.configure(state=DISABLED)

        if self.detached_items:
            self.undo_btn.configure(state=NORMAL)

        else:
            self.undo_btn.configure(state=DISABLED)


        self.remove_btn.configure(command=lambda: self.handle_delete(table, *items))
        self.undo_btn.configure(command=lambda: self.handle_undo(table))


    def _prepare_obj(self):
        self.load_images()

        self.command_sector = Frame(self.main_frame)

        self.remove_btn = Button(self.command_sector, text="Hapus", state=DISABLED, image=self._delete_image, compound=LEFT)
        self.undo_btn = Button(self.command_sector, text="Undo", state=DISABLED, image=self._undo_image, compound=LEFT)

        self.export_btn = Button(self.command_sector, text="Export", state=DISABLED, image=self._export_image, compound=LEFT, command=self._export)

        self.load_btn = Button(self.command_sector, text="Load Backup", command=self.load_)

        # Frame for item counter
        self.item_counter_frame = Frame(self.main_frame)


    def render(self):
        self._prepare_obj()

        self.main_frame.pack(fill=BOTH, expand=True)
        self.command_sector.pack(fill=X, padx=2, pady=5)
        self.remove_btn.pack(side=LEFT, padx=4)
        self.undo_btn.pack(side=LEFT, padx=4)
        self.export_btn.pack(side=LEFT)

        # table
        self.table.render()

        # render counter widget
        self.item_counter_frame.pack(anchor='w')
        Label(self.item_counter_frame, textvariable=self.item_counter_vars).pack(side=LEFT)

        self._rendered = True
