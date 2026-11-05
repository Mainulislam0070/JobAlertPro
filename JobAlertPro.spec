# -*- mode: python ; coding: utf-8 -*-
# Build with:  pyinstaller JobAlertPro.spec
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata

datas = collect_data_files("customtkinter")
try:
    datas += copy_metadata("keyring")
except Exception:
    pass

hiddenimports = [
    "plyer.platforms.win.notification",
    "pystray._win32",
    "win32ctypes.core",
] + collect_submodules("keyring.backends")

a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="JobAlertPro",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    # icon="icon.ico",   # optional: add an icon.ico next to this file and uncomment
)
