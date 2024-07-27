import appscript

from pykeynote.keynote_image import KeynoteImage
from pykeynote.keynote_movie import KeynoteMovie
from pykeynote.keynote_text_item import KeynoteTextItem
from pykeynote.keynote_layout import KeynoteLayout


class KeynoteSlide:
    def __init__(self, slide):
        self._slide = slide

    def get_name(self):
        return self._slide.name.get()
    
    def get_title(self):
        return self._slide.default_title_item.get().object_text.get()
    
    def get_body(self):
        return self._slide.default_body_item.get().object_text.get()
    
    def set_title(self,title):
        _title=self._slide.default_title_item.get()
        _title.object_text.set(title)

    def set_body(self,body):
        _body=self._slide.default_body_item.get()
        _body.object_text.set(body)
    
    def get_notes(self):
        return self._slide.presenter_notes.get()
    
    def get_slide_number(self):
        return self._slide.get().slide_number.get()

    def set_notes(self, notes):
        self._slide.presenter_notes.set(notes)
    
    def get_images(self):
        images = []
        for i in self._slide.images.get():
            images.append(KeynoteImage(i))
        return images
    
    def get_movies(self):
        movies = []
        for v in self._slide.movies.get():
            movies.append(KeynoteMovie(v))
        return movies
    
    def get_text_items(self):
        text_items = []
        for t in self._slide.text_items.get():
            text_items.append(KeynoteTextItem(t))
        return text_items
    
    def get_body_showing(self):
        return self._slide.body_showing.get()
    
    def get_title_showing(self):
        return self._slide.title_showing.get()
    
    def get_skipped(self):
        return self._slide.skipped.get()
    
    def new_image(self, file_path):
        # Add a imaged item
        k = appscript.k
        imagepath = appscript.mactypes.File(file_path)
        self._slide.make(new=k.image,with_properties={
            k.description:"THE IMAHE",k.file :imagepath,
            k.width: 100, k.height: 100
        })

    def new_movie(self, file_path):
        # Add a imaged item
        k = appscript.k
        moviepath = appscript.mactypes.File(file_path)
        self._slide.make(new=k.image,with_properties={
            k.description:"THE IMAHE",k.file :moviepath,
            k.width: 100, k.height: 100
        })

    # It's not base slide but base_layout
    def get_layout(self):
        return KeynoteLayout(self._slide.base_layout)
    
    # Todo - this needs access from slide_layout
    def set_layout(self, layout):
        self._slide.layout.set(layout)
        # Find the right master slide
        #print("our master",keynote.documents[1].slide_layouts['Title - Centre'].get().name.get())

        # app('Keynote').documents[1].current_slide.base_layout.set(app.documents[1].slide_layouts['Title - Center'])

    slide_number = property(get_slide_number)
    notes = property(get_notes, set_notes)
    name = property(get_name)
    title = property(get_title, set_title)
    body = property(get_body, set_body)
    images = property(get_images)
    movies = property(get_movies)
    text_items = property(get_text_items)
    skipped = property(get_skipped)
    body_showing = property(get_body_showing)
    title_showing = property(get_title_showing)
    layout = property(get_layout)
