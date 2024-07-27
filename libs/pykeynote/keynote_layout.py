class KeynoteLayout:
    def __init__(self, layout):
        self._layout = layout

    def get_name(self):
        return self._layout.name.get()
    name = property(get_name)
