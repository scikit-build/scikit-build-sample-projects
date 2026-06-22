import os
import sys
from pathlib import Path

# Windows ignores RPATH, so the relative path baked into _hello cannot locate
# hello.dll in the lib/ subdirectory. Register it as a DLL search directory.
if sys.platform == "win32":
    os.add_dll_directory(str(Path(__file__).parent / "lib"))

from ._hello import hello, return_two

__all__ = ("hello", "return_two")
