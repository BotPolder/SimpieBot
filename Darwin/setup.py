from setuptools import setup
APP = ['SimpieSourceCode.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'bot.ico',
 'argv_emulation': True,
 'packages': ['certifi'],
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)