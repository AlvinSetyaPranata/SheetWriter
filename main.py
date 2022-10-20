from modules.layouts import (
    main, config, changes
)
from tkinter import BOTH, Tk
from tkinter.ttk import Notebook
from modules.utils.reader import Reader
from tkinter import filedialog
from modules.handler.config import Config
from os.path import (join, dirname)


class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sheetwriter - Lite")
        self.window.geometry("600x500")
        self.window.wm_resizable(False, False)


        # define Tabs
        self.tabs = Notebook(self.window)

        self.current_config = Config(join(dirname(__file__), "modules", "default_config"))


        self.config_layout = config.ConfigLayout(self.tabs, self.update_file)
        self.changes_layout = changes.ChangesLayout(self.tabs)
        self.main_layout = main.MainLayout(self.tabs, Reader(self.config_layout.current_filename, self.current_config.get_config("all")), self.changes_layout.table.add_row)

        self.main_layout._prepare_obj()
        self.config_layout._prepare_obj()
        self.changes_layout._prepare_obj()


    def update_file(self, fname_path):
        self.main_layout.load_autosearch(Reader(fname_path, self.current_config.get_config("all")))


    def run(self):
        self.tabs.pack(fill=BOTH, expand=True)

        self.main_layout.render()
        self.config_layout.render()
        self.changes_layout.render()

        self.tabs.add(self.main_layout.main_frame, text="Main")
        self.tabs.add(self.config_layout.main_frame, text="Konfigurasi")
        self.tabs.add(self.changes_layout.main_frame, text="Status")


        self.window.mainloop()


Main().run()