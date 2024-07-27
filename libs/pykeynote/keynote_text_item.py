class KeynoteTextItem:
    def __init__(self, text_item):
        self._text_item = text_item
    
    def get_text(self):
        return self._text_item.object_text.get()

    def get_height(self):
        return self._text_item.height.get()
    
    def get_width(self):
        return self._text_item.width.get()
    
    # Position is tuple
    def get_x(self):
        return self._text_item.position.get()[0]
    
    def get_y(self):
        return self._text_item.position.get()[1]
    
    # string
    def get_font(self):
        return self._text_item.object_text.font.get()
    
    # It uses an RGB model where you provide a 16-bit number for each colour. These values can be derived by multiplying the RGB value by 257. For example, Blueberry has values of {0, 0, 255}; multiply by 257 and you get the {0, 0, 65535} below. Conversely, if you divide each of the 'added text' colours of {25441, 10793, 42404} by 257, you end up with 99/42/165 (or #632AA5).
    # https://apple.stackexchange.com/questions/381590/using-applescript-to-change-text-color-in-keynote

    # RGB color
    def get_color(self):
        return self._text_item.object_text.color.get()
    
    # 12.0
    def get_size(self):
        return self._text_item.object_text.size.get()
    # color
    # font
    # size

    width = property(get_width)
    height = property(get_height)
    text = property(get_text)
    x= property(get_x)
    y = property(get_y)
    font = property(get_font)
    color = property(get_color)
    size = property(get_size)
    