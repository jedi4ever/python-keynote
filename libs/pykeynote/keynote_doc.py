import appscript
import os

from pykeynote.keynote_slide import KeynoteSlide
from pykeynote.keynote_layout import KeynoteLayout
from pykeynote.keynote_theme import KeynoteTheme

class KeynoteDoc:
    def __init__(self, doc):
        self._doc = doc

    def get_slides(self):
        slides = []
        for s in self._doc.slides.get():
            slides.append(KeynoteSlide(s))
        return slides
    
    def get_layouts(self):
        layouts = []
        for l in self._doc.slide_layouts.get():
            layouts.append(KeynoteLayout(l))
        return layouts
    
    def close(self):
        k = appscript.k
        # k.ask , k.yes , k.no
        self._doc.close(saving=k.no)

    def new_slide(self):
        k = appscript.k
        slide = self._doc.make(new=k.slide)
        return KeynoteSlide(slide)
    
    def move_to(self, slide_number, to):
        self._doc.slides[slide_number].move(to=self._doc.slides[to])

    # Duplicate range & after
    # app('Keynote').documents[1].slides[con.slides[1]:con.slides[2]].duplicate(to=app.documents[1].slides[2].after)
    def duplicate_slide(self, number):
        slide = self._doc.slides[number].duplicate()
        return KeynoteSlide(slide)
    
    def duplicate_slides_to(self,begin,end,to):
        self._doc.slides[begin:end].duplicate(to=self._doc.slides[to].after)
    
    def del_slide(self,number):
        self._doc.slides[number].delete()
        #app('Keynote').documents[1].slides[its.default_title_item.object_text.contains('2012')].delete()



    def get_current_slide(self):
        return KeynoteSlide(self._doc.current_slide.get())
    # returns a raw slide

    def get_theme(self):
        return KeynoteTheme(self._doc.document_theme.get())

    # number of slide (inclusive skipped slides)
    def set_slide(self,number):
        self._doc.current_slide.set(self._doc.slides[number])

    # use the slide number (this is only for visibile slides)
    def set_slide_nr(self,number):
        k = appscript.k
        self._doc.current_slide.set(self._doc.slides[k.its.slide_number == number].slides[1])

    # TODO : maybe this belongs to the keynote class ?
    def start(self,slide_number=1):
        self._doc.start(from_=self._doc.slides[slide_number])

    def stop(self):
        self._doc.stop()

    #def show_next(self):
    #    self._doc.show_next()
    #    app('Keynote').show_next()
    #app('Keynote').documents[1].stop()
    #    app('Keynote').show_previous()

    
    def save(self, file_path):
        filepath = appscript.mactypes.File(os.path.abspath(file_path))
        self._doc.save(in_=filepath)

    def export_as_images(self,slides_dir):
        k = appscript.k
        outpath = appscript.mactypes.File(slides_dir)
        self._doc.export(as_=k.slide_images, to=outpath, with_properties = {
            k.export_style: k.IndividualSlides,
            k.compression_factor: 0.9,
            k.image_format: k.JPEG,
            k.all_stages: True,
            k.skipped_slides: False
        })

    def export_as_pdf(self,file_path):
        print("exporting as pdf")
        # Use encrypted_default_value
        # https://iworkautomation.com/keynote/document-export.html
#        k = appscript.k
#        outpath = appscript.mactypes.File(file_path)
#        self._doc.export(as_=k.PDF, to=outpath, with_properties = {
#            k.all_stages: True,
#            k.skipped_slides: False
#        })

    # quit ?
    # close ?

    slides = property(get_slides)
    layouts = property(get_layouts)
    theme = property(get_theme)
    current_slide = property(get_current_slide)