from modules.handler.autocomplete import AutoSearch
from modules.components.search import Search
from . import *
from tkinter.messagebox import showerror, showinfo, showwarning



class MainLayout(BaseLayout):
    def __init__(self, parent, f_handler, onsave, backuper):
        """"
        Parent should Notebook object
        :f_handler 
        """
        super().__init__()

        self.parent = parent
        self.autosearch = None
        self.backuper = backuper
        self.date_value = StringVar()
        self.month_value = StringVar()
        self.year_value = StringVar()
        self.onsave = onsave

        self.load_autosearch(f_handler)

    def load_autosearch(self, f_handler):
        if not f_handler:
            return

        self.autosearch = AutoSearch(f_handler, self.alert)


    def alert(self, type_, msg):
        if type_ == "error":
            showerror("Error", msg)
        elif type_ == "info":
            showinfo("Info", msg)
        elif type_ == "warning":
            showwarning("Warning", msg)


    def handle_update_input(self, code, delete=False):
        if delete:
            self.name_input.configure(state="normal")
            self.name_input.delete(0, END)
            self.name_input.configure(state="readonly")
            return

        self.name_input.configure(state="normal")
        self.name_input.delete(0, END)
        self.name_input.insert(0, self.autosearch.search_by_code(code)[0][1].value)
        self.name_input.configure(state="readonly")


    def handle_autosearch(self):
        matches = self.autosearch.search_by_code(self.code_input.get())

        if not matches:
            self.search_.switch_off()
            self.handle_update_input("", delete=True)
            return

        if len(matches) == 1:
            self.search_.switch_off()
            self.handle_update_input(matches[0][0].value)
            return


        for match in tuple(reversed(matches)):
            self.search_.insert(match[0].value)


    def handle_input_focus(self, event):
        self.search_.switch_off()  
        
        if event.keysym == "Escape":
            return

        self.validate_length(event, 6)

        # elif event.keysym == "Up" or event.keysym == "Down":
        #     self.search_.set_focus()

        self.search_.switch_on()
        self.handle_autosearch()


    def validate_length(self, event, max_length, keyword_exc="BackSpace"):
        _widget = event.widget
        if len(_widget.get()) > max_length and event.keysym != keyword_exc:
            _str = _widget.get()[:max_length]
            _widget.delete(0, END)
            _widget.insert(0, _str)



    def accept_changes(self):

        if not self.name_input.get():
            self.alert("error", "Nama barang tidak boleh kosong!")
            return

        if not self.autosearch.search_years(self.year_opt.get()):
            self.alert("error", "Tahun tidak ditemukan")
            return

        if not self.autosearch.find_month_coord(self.year_opt.get(), self.month_opt.get()):
            self.alert("error", "Bulan tidak ditemukan")
            return

        if not self.value_input.get().isnumeric():
            self.alert("error", "Nilai harus berupa angka")
            return

        _data = (str(self.code_input.get()), str(self.name_input.get()), str(self.month_opt.get()), str(self.year_opt.get()), str(self.value_input.get()))

        self.alert("info", "Perubahan Tersimpan!")
        self.onsave(self.autosearch, _data)
        self._clear_widget()
        self.code_input.focus_force()
        self.backuper.listen(_data)

    def _clear_widget(self):
        self.code_input.delete(0, END)
        self.month_opt.delete(0, END)
        self.year_opt.delete(0, END)
        self.value_input.delete(0, END)

        self.name_input.configure(state=NORMAL)
        self.name_input.delete(0, END)
        self.name_input.configure(state="readonly")

    def _prepare_obj(self):
        self.main_frame = Frame(self.parent)

        self.container = Frame(self.main_frame)

        # CodeField Group
        self.code_group = Frame(self.container)

        self.code_label = Label(self.code_group, text="Kode Barang")
        self.code_input = Entry(self.code_group)
        self.code_input.bind("<KeyRelease>", self.handle_input_focus)
        self.code_input.bind("<FocusOut>", lambda x: self.search_.switch_off())
        self.code_input.bind("<Return>", lambda x: self.month_opt.focus_force())

        self.search_ = Search(self.parent, self.handle_update_input)


        # NameField Group
        self.name_group = Frame(self.container)

        self.name_label = Label(self.name_group, text="Nama Barang")
        self.name_input = Entry(self.name_group, state="readonly", fg="black")


        # Datetime Group
        self.datetime_group = Frame(self.container)


        # Month Group
        self.month_group = Frame(self.datetime_group)

        self.month_label = Label(self.month_group, text="Bulan", pady=5)
        self.month_opt = Entry(self.month_group, width=5)
        self.month_opt.bind("<Return>", lambda x: self.year_opt.focus_force())
        self.month_opt.bind("<KeyRelease>", lambda x: self.validate_length(x, 2))


        #Year Group
        self.year_group = Frame(self.datetime_group)

        self.year_label = Label(self.year_group, text="Tahun", pady=5)
        self.year_opt = Entry(self.year_group, width=5)
        self.year_opt.bind("<Return>", lambda x: self.value_input.focus_force())
        self.year_opt.bind("<KeyRelease>", lambda x: self.validate_length(x, 4))


        #Value Group
        self.value_group = Frame(self.container)

        self.value_label = Label(self.value_group, text="Nilai")
        self.value_input = Entry(self.value_group)
        self.value_input.bind("<Return>", lambda x: self.accept_changes())
    
        self.action_btn = Button(self.container, text="Simpan Perubahan", command=self.accept_changes)


    def render(self):
        self._prepare_obj()

        self.main_frame.pack(fill=BOTH, expand=True)

        self.container.pack(anchor=CENTER, expand=True)

        self.code_group.grid(row=0, column=0, padx=10, pady=10)
        self.name_group.grid(row=0, column=1, padx=10, pady=10)
        self.datetime_group.grid(row=1, column=0, padx=10, pady=10)
        self.value_group.grid(row=1, column=1, pady=10, padx=10)
        self.action_btn.grid(row=2, column=0, columnspan=2)


        self.month_group.pack(side=LEFT, padx=12)
        self.year_group.pack(side=LEFT, padx=12)

        self.code_label.pack(anchor='w')
        self.code_input.pack(ipady=2)
        self.search_.render()

        self.name_label.pack(anchor='w')
        self.name_input.pack(ipady=2)

        self.month_label.pack()
        self.month_opt.pack()

        self.year_label.pack()
        self.year_opt.pack()

        self.value_label.pack(anchor='w')
        self.value_input.pack(ipady=2)


        self._rendered = True
