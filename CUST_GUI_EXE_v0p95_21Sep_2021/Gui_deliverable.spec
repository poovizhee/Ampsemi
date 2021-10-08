# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:\\VRM\\GUI_SH_folder\\Main Files 22 Sep v095\\Main FIles\\Gui_deliverable.py'],
             pathex=['D:\\VRM\\GUI_SH_folder\\CUST_GUI_EXE_v0p95_21Sep_2021'],
             binaries=[],
             datas=[],
             hiddenimports=['clr'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Gui_deliverable',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Gui_deliverable')
