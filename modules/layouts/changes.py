from tkinter.filedialog import asksaveasfilename
from . import *
from modules.components.table import Table
from PIL import Image, ImageTk
from modules.utils.writer import Writer


class ChangesLayout(BaseLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.main_frame = Frame(self.parent)
        self.row_id = []
        self.detached_items = set()

        self.table = Table(self.main_frame, ("Kode Barang", "Nama Barang", "Bulan", "Tahun","Kuantitas"), onSelect=self.handle_select, mode="extended", onChange=self.check_table)

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

        self.remove_btn.configure(state=DISABLED)
        self.undo_btn.configure(state=NORMAL)

        self.check_table()
        

    def handle_undo(self, table):
        for item in self.detached_items:
            table.move(item, '', 0)

        self.detached_items.clear()
        self.undo_btn.configure(state=DISABLED)

        self.check_table()

    def check_table(self):
        if not self.table._bodies:
            self.export_btn.configure(state=DISABLED)
            return

        self.export_btn.configure(state=NORMAL)


    def _export(self):
        _ftarget = asksaveasfilename(defaultextension=".xlsx", filetypes=())

        w  = Writer()



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

        self.export_btn = Button(self.command_sector, text="Export", state=DISABLED, image=self._export_image, compound=LEFT, commnad=self._export)


    def render(self):
        self._prepare_obj()

        self.main_frame.pack(fill=BOTH, expand=True)
        self.command_sector.pack(fill=X, padx=2, pady=5)
        self.remove_btn.pack(side=LEFT, padx=4)
        self.undo_btn.pack(side=LEFT, padx=4)
        self.export_btn.pack(side=LEFT)

        # table
        self.table.render()
        self._rendered = True
