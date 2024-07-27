class KeynoteImage:
    def __init__(self, image):
        self._image = image

    def get_file_name(self):
        return self._image.file_name.get()

    def get_height(self):
        return self._image.height.get()
    
    def get_width(self):
        return self._image.width.get()
    
    def get_description(self):
        return self._image.description.get()
    
    width = property(get_width)
    height = property(get_height)
    file_name = property(get_file_name)
    description = property(get_description)