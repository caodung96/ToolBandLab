import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {"build_exe": {"includes": "atexit"}}

executables = [Executable("Tool.py", base=base)]

setup(
    name="ToolSendBeat",
    version="0.1",
    description="ToolSendBeat",
    options=options,
    executables=executables,
)