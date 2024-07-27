class KeynoteShape:
    def __init__(self, shape):
        self._shape = shape
    
    def get_height(self):
        return self._shape.height.get()
    
    def get_width(self):
        return self._shape.width.get()
    
    def get_text(self):
        return self._shape.object_text.get()
    
    def get_opacity(self):
        return self._shape.opacity.get()
    
    
    text = property(get_text)
    width = property(get_width)
    height = property(get_height)
    opacity = property(get_opacity)
