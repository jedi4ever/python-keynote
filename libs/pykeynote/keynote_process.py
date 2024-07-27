import appscript
from pykeynote.keynote_window import KeynoteWindow

class KeynoteProcess():
    def __init__(self):
        self._process = appscript.app('System Events').processes['Keynote']

    def get_windows(self):
        _windows=self._process.windows.get()
        windows = []
        for window in _windows:
            windows.append(KeynoteWindow(window))
        return windows
    
    def get_window_by_name(self,name):
        window = self._process.windows[name]
        if window:
            return KeynoteWindow(window)
    
    def add_rectangle(self):
        self._process.menu_bars[0].menu_bar_items['Insert'].menus[0].menu_items['Shape'].menus[0].menu_items['Rectangle'].click()


    def add_rounded_rectangle(self):
        self._process.menu_bars[0].menu_bar_items['Insert'].menus[0].menu_items['Shape'].menus[0].menu_items['Rounded Rectangle'].click()


    windows = property(get_windows)