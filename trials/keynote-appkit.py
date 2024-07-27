#!/usr/bin/env python
import appscript
import os
from contextlib import closing
import itertools



def create_slides():
    keynote = appscript.app('Keynote')
    # Create a new doc
    k = appscript.k

    # List themes
    themes = keynote.themes.get()
    my_theme = None
    for t in themes:
        theme = t.get()
        theme_name = theme.name.get()
        # Select the theme to create the doc
        if theme_name == "Black":
            print(theme_name)
            my_theme = t
    # Add a doc with defaults
    #doc = keynote.make(new=appscript.k.document)


    # Add a doc with a theme
    doc = keynote.make(new=appscript.k.document,with_properties={
        k.document_theme :my_theme,
        k.width: 1024,
        k.height: 768
    })
    print(doc.get())

    # List master slides
    # It's called slide_layouts , not masters !!!!
    # found it through AS Translate of script !
    masters= doc.slide_layouts.get()
  #  print("master",masters.name)
    for m in masters:
        print("master", m.get().name.get())

    # Find the right master slide
    print("our master",keynote.documents[1].slide_layouts['Title - Centre'].get().name.get())

    # app('Keynote').documents[1].current_slide.base_layout.set(app.documents[1].slide_layouts['Title - Center'])


    # Add a new slide
    doc.make(new=appscript.k.slide)
    # Get the slides
    slides = doc.slides.get()
    # Set the text for the first slide
    slide1 = slides[0].get()

    # Set title
    title=slide1.default_title_item.get()
    title.object_text.set("MAAAA")

    # Set body
    body = slide1.default_body_item.get()
    body.object_text.set("WOOOOO")
    # https://github.com/macintoshhelper/keynote-js/blob/master/src/slide.ts#L130
    # font & color - TODO

    # Set the notes
    slide1.presenter_notes.set("NOTES")
#    print("base",slide1.base_layout().get())

    # Add a text item
    slide1.make(new=k.text_item, with_properties={k.object_text: "WOEF"})

    # Add a imaged item
    imagepath = appscript.mactypes.File("image.jpeg")
    slide1.make(new=k.image,with_properties={k.description:"THE IMAHE",k.file :imagepath, k.width: 100, k.height: 100})

    # Add video item
    videopath = appscript.mactypes.File("movie.mov")
    # https://iworkautomation.com/keynote/media-items-movie.html
    # Keynote does not have a movie item to add , use the image type
    # hmm used to work, but not after switching the theme??
    slide1.make(new=k.image,with_properties={k.file:videopath, k.width: 100, k.height: 100})
    #  k.rotation: 90 - not working

    # Get the text items
    items = slide1.text_items.get()
    # Change them
    #for item in items:
    #    item.object_text.set("hello")
    doc.save(in_=appscript.mactypes.File(os.path.abspath("bla2.key")))

def export_slides():
    filename="bla2.key"
    filename = os.path.abspath(filename)
    slidesDir="p"
    keynote = appscript.app('Keynote')
    outpath = appscript.mactypes.File(slidesDir)
    k = appscript.k
    keynote_file = appscript.mactypes.File(filename)

    with closing(keynote.open(keynote_file)) as doc:

        slides =  doc.slides.get()
        for s in slides:
            print("slide",s.get().slide_number.get())
            images = s.get().images.get()
            for i in images:
                image = i.get()
                print("desc",image.description.get())
                #print("object description",image.object_description)
                # Id , file_name , description

                # https://appscript.sourceforge.io/py-appscript/doc_3x/mactypes-manual/03_fileclass.html
               # print("file id",str(image.file.id))
               # print("file des",str(image.file.description))
               # print("file file_name",str(image.file.file_name))

                print("reflection showing",image.reflection_showing.get())

                print("width",image.width.get())
                print("image file name",image.file_name.get())

        notes = doc.slides.presenter_notes()
        skipped = doc.slides.skipped()
        notes = list(itertools.compress(notes, [not s for s in skipped]))

        doc.export(as_=k.slide_images, to=outpath, with_properties = {
            k.export_style: k.IndividualSlides,
            k.compression_factor: 0.9,
            k.image_format: k.JPEG,
            k.all_stages: True,
            k.skipped_slides: False
        })

#create_slides()
#export_slides()