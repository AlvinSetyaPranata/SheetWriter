from modules.handler.config import Config
from . import *
from tkinter.filedialog import askopenfilename

class ConfigLayout(BaseLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.handler = Config(Config.resolve_parent_path(__file__, "default_config", parent_=1))
        self.current_filename = askopenfilename(filetypes=(("Excel 2003", ".xls"), ("Excel 2007", ".xlsx")))

    def apply_configuration(self, event):
        self.handler.add_config(
            {
                "year_coords" : self.year_conf_input.get(),
                "name_coords" : self.product_conf_input.get(),
                "code_coords" : self.code_conf_input.get()
            }
        )

    def file_load(self):
        self.current_filename = askopenfilename(filetypes=(("Excel 2003", ".xls"), ("Excel 2007", ".xlsx")))

        self.fname_entry.configure(state=NORMAL)
        self.fname_entry.delete(0, END)
        self.fname_entry.insert(0, self.current_filename)
        self.fname_entry.configure(state="readonly")

    def conf_load(self):
        year = self.handler.get_config("year_coords")
        product = self.handler.get_config("name_coords")
        code = self.handler.get_config("code_coords")


        self.year_conf_input.insert(0, year)
        self.product_conf_input.insert(0, product)
        self.code_conf_input.insert(0, code)



    def _prepare_obj(self):
        self.main_frame = Frame(self.parent)
        self.container = Frame(self.main_frame)


        self.file_configuration = LabelFrame(self.container, text="Konfigurasi File")
        self.cell_configuration = LabelFrame(self.container, text="Konfigurasi Excel")
        
        # File Group
        self.fname_label = Label(self.file_configuration, text="Nama File")
        self.fname_entry = Entry(self.file_configuration, state="readonly", fg="black")
        self.load_btn = Button(self.file_configuration, text="Muat File", command=self.file_load)

        # Cell Group
        self.year_conf_group = Frame(self.cell_configuration)
        self.year_conf_label = Label(self.year_conf_group, text="Cell tahun pada Excel")
        self.year_conf_input = Entry(self.year_conf_group)


        self.product_conf_group = Frame(self.cell_configuration)
        self.product_conf_label = Label(self.product_conf_group, text="Cell nama pada Excel")
        self.product_conf_input = Entry(self.product_conf_group)

        self.code_conf_group = Frame(self.cell_configuration)
        self.code_conf_label = Label(self.code_conf_group, text="Cell kode pada Excel")
        self.code_conf_input = Entry(self.code_conf_group)

        self.apply_btn = Button(self.cell_configuration, text="Simpan perubahan")


    def render(self):
        self._prepare_obj()
        self.conf_load()

        self.fname_entry.configure(state="normal")
        self.fname_entry.insert(0, self.current_filename)
        self.fname_entry.configure(state="readonly")


        self.main_frame.pack(fill=BOTH, expand=True)
        self.container.pack(expand=True)

        self.file_configuration.grid(row=0, column=0, ipadx=20, ipady=5, pady=10)
        self.cell_configuration.grid(row=1, column=0, ipadx=20, ipady=5)

        # File sections
        self.fname_label.grid(row=0, column=0, padx=10)
        self.fname_entry.grid(row=0, column=1, padx=10)
        self.load_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Excel sections
        self.year_conf_group.pack(pady=5)
        self.year_conf_label.pack(side=LEFT)
        self.year_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)
        
        
        self.product_conf_group.pack(pady=5)
        self.product_conf_label.pack(side=LEFT)
        self.product_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)

        self.code_conf_group.pack(pady=5)
        self.code_conf_label.pack(side=LEFT)
        self.code_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)

        self.apply_btn.pack()

        self._rendered = True