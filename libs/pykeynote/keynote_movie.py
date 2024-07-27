class KeynoteMovie:
    def __init__(self, movie):
        self._movie = movie
    
    def get_file_name(self):
        return self._movie.file_name.get()

    def get_height(self):
        return self._movie.height.get()
    
    def get_width(self):
        return self._movie.width.get()
    
    def get_volume(self):
        return self._movie.movie_volume.get()
    
    def get_opacity(self):
        return self._movie.opacity.get()
    
    # Doesn't seem to exit ?
    #def get_rotation(self):
    #    return self._movie.rotation.get()
    
    # TODO Reflection
    
    width = property(get_width)
    height = property(get_height)
    file_name = property(get_file_name)
    volume = property(get_volume)
    opacity = property(get_opacity)
    #rotation = property(get_rotation)