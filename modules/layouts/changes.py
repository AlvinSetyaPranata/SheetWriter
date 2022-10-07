from . import *
from modules.utils.table import Table



class ChangesLayout(BaseLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.main_frame = Frame(self.parent)

    def _prepare_obj(self):

        self.command_sector = Frame(self.main_frame)

        self.remove_btn = Button(self.command_sector, text="Hapus", state=DISABLED)
        self.undo_btn = Button(self.command_sector, text="Undo", state=DISABLED)

        self.table = Table(self.main_frame, ("Kode Barang", "Nama Barang", "Tanggal", "Kuantitas"))



    def render(self):
        self._prepare_obj()


        self.main_frame.pack(fill=BOTH, expand=True)
        self.command_sector.pack(fill=X, padx=2, pady=5)
        self.remove_btn.pack(side=LEFT, padx=4)
        self.undo_btn.pack(side=LEFT)

        # table
        self.table.render()
        self._rendered = True
