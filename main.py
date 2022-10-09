from modules.layouts import (
    main, config, changes
)
from tkinter import BOTH, Tk
from tkinter.ttk import Notebook


class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sheetwriter - Lite")
        self.window.geometry("500x500")
        self.window.wm_resizable(False, False)


        # define Tabs
        self.tabs = Notebook(self.window)

        self.main_layout = main.MainLayout(self.tabs)
        self.config_layout = config.ConfigLayout(self.tabs)
        self.changes_layout = changes.ChangesLayout(self.tabs)

        self.main_layout._prepare_obj()
        self.config_layout._prepare_obj()
        self.changes_layout._prepare_obj()


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