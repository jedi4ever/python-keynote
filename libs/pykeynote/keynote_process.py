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
    
    windows = property(get_windows)