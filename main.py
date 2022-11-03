from modules.layouts import (
    main, config, changes
)
from tkinter import BOTH, Tk
from tkinter.ttk import Notebook
from modules.utils.reader import Reader
from modules.handler.config import Config
from os.path import (join, dirname)
from modules.utils.backuper import Backuper, Loader
from tkinter.messagebox import askyesno


class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sheetwriter - Lite")
        self.window.geometry("600x500")
        self.window.wm_resizable(False, False)

        self.window.wm_protocol("WM_DELETE_WINDOW", self.before_close)


        # define Tabs
        self.tabs = Notebook(self.window)

        # Loader

        self.current_config = Config(join(dirname(__file__), "modules", "default_config"))
        self.config_layout = config.ConfigLayout(self.tabs, self.update_file)

        # backuper
        self.backuper = Backuper(5)
        self.loader = Loader()

        # reader and other layouts

        _reader = Reader(self.config_layout.current_filename, self.current_config.get_config("all"))

        self.changes_layout = changes.ChangesLayout(self.tabs, self.config_layout.get_filename, _reader, self.loader)
        self.main_layout = main.MainLayout(self.tabs, _reader, self.changes_layout.handle_add, self.backuper)

        self.main_layout._prepare_obj()
        self.config_layout._prepare_obj()
        self.changes_layout._prepare_obj()


    def update_file(self, fname_path):
        self.main_layout.load_autosearch(Reader(fname_path, self.current_config.get_config("all")))


    def report_callback_exception(self, exec, val, tb):
        self.alert("error", val)
        self.window.destroy()


    def before_close(self):
        if askyesno("Warning", "Apakah anda ingin menghapus file backup?"):
            self.backuper.close()

        self.window.destroy()
            

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