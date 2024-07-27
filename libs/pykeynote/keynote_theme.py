class KeynoteTheme:
    def __init__(self, theme):
        self._theme = theme

    def get_name(self):
        return self._theme.name.get()
    
    def get_id(self):
        return self._theme.id.get()
    
    name = property(get_name)
    id = property(get_id)