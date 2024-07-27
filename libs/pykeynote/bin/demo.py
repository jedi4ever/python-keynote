#!/usr/bin/env python

from pykeynote.keynote_app import KeynoteApp

def demo():
    keynote = KeynoteApp()
#    keynote.quit()
    keynote.open("bla2.key")

    for t in keynote.themes:
        print("theme name",t.name)
        print("theme id",t.id)

    for d in keynote.docs:
        for l in d.layouts:
            print("layout",l.name)
        d.set_slide(1)
        print("Document theme", d.theme.name)
        #d.del_slide(2)
        for s in d.slides:
        #    print(s.name)
            print("slide nr",s.slide_number)
            print("title",s.title)
            print("body",s.body)
            print("notes",s.notes)
            print("slide body showing",s.body_showing)
            print("slide title showing",s.title_showing)
            print("slide skipped",s.skipped)
            print("slide layout",s.layout.name)

            for t in s.text_items:
                print("text text", t.text)
                print("text width",t.width)
                print("text height",t.height)
                print("text font",t.font)
                print("text size",t.size)
                print("text color",t.color)
                print("text x",t.x)
                print("text y",t.y)

            for i in s.images:
                print("image file name",i.file_name)
                print("image width",i.width)
                print("image height",i.height)
                print("image description",i.description)
            for m in s.movies:
                print("movie file name",m.file_name)
                print("movie width",m.width)
                print("movie height",m.height)
                print("movie volume",m.volume)
                print("movie opacity",m.opacity)
                #print("move.rotation",m.rotation)

        d.start()
        d.stop()
        d.close()

    keynote.quit()


def main():
    demo()

if __name__ == "__main__":
    main()
