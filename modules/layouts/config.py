from . import *


class ConfigLayout(BaseLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

    def _prepare_obj(self):
        self.main_frame = Frame(self.parent)
        self.container = Frame(self.main_frame)


        self.cell_configuration = LabelFrame(self.container, text="Konfigurasi Excel")

        self.year_conf_group = Frame(self.cell_configuration)
        self.year_conf_label = Label(self.year_conf_group, text="Cell tahun pada Excel")
        self.year_conf_input = Entry(self.year_conf_group)

        self.month_conf_group = Frame(self.cell_configuration)
        self.month_conf_label = Label(self.month_conf_group, text="Cell bulan pada Excel")
        self.month_conf_input = Entry(self.month_conf_group)

        self.product_conf_group = Frame(self.cell_configuration)
        self.product_conf_label = Label(self.product_conf_group, text="Cell nama pada Excel")
        self.product_conf_input = Entry(self.product_conf_group)

        self.code_conf_group = Frame(self.cell_configuration)
        self.code_conf_label = Label(self.code_conf_group, text="Cell kode pada Excel")
        self.code_conf_input = Entry(self.code_conf_group)

        self.apply_btn = Button(self.cell_configuration, text="Simpan perubahan")


    def render(self):
        self._prepare_obj()


        self.main_frame.pack(fill=BOTH, expand=True)
        self.container.pack(expand=True)

        self.cell_configuration.grid(row=0, column=0, ipadx=20, ipady=5)

        # Excel sections
        self.year_conf_group.pack(pady=5)
        self.year_conf_label.pack(side=LEFT)
        self.year_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)
        
        self.month_conf_group.pack(pady=5)
        self.month_conf_label.pack(side=LEFT)
        self.month_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)
        
        self.product_conf_group.pack(pady=5)
        self.product_conf_label.pack(side=LEFT)
        self.product_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)

        self.code_conf_group.pack(pady=5)
        self.code_conf_label.pack(side=LEFT)
        self.code_conf_input.pack(side=LEFT, padx=2, ipadx=2, ipady=2)

        self.apply_btn.pack()

        self._rendered = True