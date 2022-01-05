from setuptools import setup

APP = ['my_project_3.py']
APP_NAME = "Calc"

OPTIONS = {
    'argv_emulation': True,
    'includes': ('tkinter'),
    # 'iconfile': 'images/ship.icns'
}
setup(
    name=APP_NAME,
    app=APP,
    # data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)