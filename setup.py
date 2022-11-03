import cx_Freeze as cf
import sys

if sys.platform == "win32":
	base = "Win32GUI"

executable = [cf.Executable("main.py", base=base)]
packages = ["tkinter", "os", "xlwt", "xlrd", "openpyxl", "json", "modules"]

cf.setup(
	name = "Sheetwriter V2.0",
	options = {"build_exe" : {"packages" : packages, "include_files" : ["assets/delete.png", "assets/undo.png", "assets/export.png", "modules/default_config.json"]}},
	executables=executable,
        author="Ahareno Pranata"
	)
