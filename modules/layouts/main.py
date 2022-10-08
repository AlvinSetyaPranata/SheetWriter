from modules.handler.autocomplete import AutoSearch
from modules.utils.search import Search
from . import *


class MainLayout(BaseLayout):
    def __init__(self, parent, data={"year" : (), "month" :  (), "date" : (), "name" : (), "code" : ()}):
        """"
        Parent should Notebook object
        """
        super().__init__()

        self.parent = parent

        self.date_value = StringVar()
        self.month_value = StringVar()
        self.year_value = StringVar()

        self.year_data = data["year"]
        self.month_data = data["month"]
        self.date_data = data["date"]


        self.autosearch = AutoSearch(data["name"])


    def handle_autosearch(self, event):
        matches = self.autosearch.search(event.keysym)


    def _prepare_obj(self):
        self.main_frame = Frame(self.parent)

        self.container = Frame(self.main_frame)

        # CodeField Group
        self.code_group = Frame(self.container)

        self.code_label = Label(self.code_group, text="Kode Barang")
        self.code_input = Entry(self.code_group)
        self.code_input.bind("<KeyRelease>", self.handle_autosearch)
        self.search_ = Search(self.code_group)


        # NameField Group
        self.name_group = Frame(self.container)

        self.name_label = Label(self.name_group, text="Nama Barang")
        self.name_input = Entry(self.name_group, state="readonly")


        # Datetime Group
        self.datetime_group = Frame(self.container)

        # date group
        self.date_group = Frame(self.datetime_group)

        self.date_label = Label(self.date_group, text="Tanggal", pady=5)
        self.date_opt = Entry(self.date_group, width=5)

        # Month Group
        self.month_group = Frame(self.datetime_group)

        self.month_label = Label(self.month_group, text="Bulan", pady=5)
        self.month_opt = Entry(self.month_group, width=5)

        #Year Group
        self.year_group = Frame(self.datetime_group)

        self.year_label = Label(self.year_group, text="Tahun", pady=5)
        self.year_opt = Entry(self.year_group, width=5)


        #Value Group
        self.value_group = Frame(self.container)

        self.value_label = Label(self.value_group, text="Nilai")
        self.value_input = Entry(self.value_group)
    
        self.action_btn = Button(self.container, text="Simpan Perubahan")

    def render(self):
        self._prepare_obj()

        self.main_frame.pack(fill=BOTH, expand=True)

        self.container.pack(anchor=CENTER, expand=True)

        self.code_group.grid(row=0, column=0, padx=10, pady=10)
        self.name_group.grid(row=0, column=1, padx=10, pady=10)
        self.datetime_group.grid(row=1, column=0, padx=10, pady=10)
        self.value_group.grid(row=1, column=1, pady=10, padx=10)
        self.action_btn.grid(row=2, column=0, columnspan=2)


        self.date_group.pack(side=LEFT, padx=12)
        self.month_group.pack(side=LEFT, padx=12)
        self.year_group.pack(side=LEFT, padx=12)

        self.code_label.pack(anchor='w')
        self.code_input.pack(ipady=2)
        self.search_.render()

        self.name_label.pack(anchor='w')
        self.name_input.pack(ipady=2)

        self.date_label.pack()
        self.date_opt.pack(ipady=2)

        self.month_label.pack()
        self.month_opt.pack()

        self.year_label.pack()
        self.year_opt.pack()

        self.value_label.pack(anchor='w')
        self.value_input.pack(ipady=2)


        self._rendered = True
