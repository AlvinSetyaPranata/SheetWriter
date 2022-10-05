from . import *


class ConfigLayout(BaseLayout):
    def __init__(self, parent, **handlers):
        super().__init__(**handlers)

        self.parent = parent

    def _prepare_obj(self):
        self.main_frame = Frame(self.parent)
        self.container = Frame(self.main_frame)


        self.file_group = LabelFrame(self.container, text="Opsi file")
        
        self.file_output_group = Frame(self.file_group)
        self.fout_label = Label(self.file_output_group, text="Nama file output")
        self.fout_input = Entry(self.file_group)



    def render(self):
        self._prepare_obj()


        self.main_frame.pack(fill=BOTH, expand=True)
        self.container.place(y=500//2-70, x=40)

        self.file_group.grid(row=0, column=0, ipadx=20, ipady=20)
        
        self.file_output_group.pack()
        self.fout_label.pack(anchor='w')
        self.fout_input.pack()


        self._rendered = True