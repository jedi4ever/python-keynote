#!/usr/bin/env python3
# https://discussions.apple.com/thread/7565876?sortBy=best
# https://github.com/nodejs/node-gyp/issues/569

# install xcode via appstore
# sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
# sdef /Applications/App.app > App.sdef
# sdp -fh --basename App App.sdef
# sbhc.py App.h
# sbsc.py App.sdef

# https://github.com/AdulteTerrible/DuplicateAndRotateKeynoteDocumentDroplet/blob/e2294057cd783ea6ee38b77883deb858c8cf1606/Script
# https://pyobjc.readthedocs.io/en/latest/core/intro.html

#       ../meson.build:29:9: ERROR: Dependency 'gobject-introspection-1.0' is required but not found.
#  brew install pygobject3


import objc

import os 

from Foundation import NSObject, NSURL
from ScriptingBridge import SBApplication , SBObject



# export Keynote document to images using the exportTo function


def info_keynote(file_path):
    Keynote = SBApplication.applicationWithBundleIdentifier_("com.apple.iWork.Keynote")
    #doc = Keynote.open_("myfile.key")
    #print(doc)
    Keynote.activate()

    docs = Keynote.documents()
    print(docs[0].name())

    doc = docs[0]
    print(doc.height())
    print(doc.width())

    slides = doc.slides()
    for slide in slides:   
        print("Slide #",slide.slideNumber())
        print("Skipped",slide.skipped())
        print("base layout", slide.baseLayout().get())
        t=(slide.defaultTitleItem().objectText())
        print(t.get())
        images = slide.images()   
        for image in images:
            print(image.className())
            print(image.file())
            print(image.fileName().get())
            print(image.height())
            print(image.width())
        for item in slide.textItems():
            print("text",item.objectText().get())
        #print(slide.text())

def export_slide():
    Keynote = SBApplication.applicationWithBundleIdentifier_("com.apple.iWork.Keynote")
    # https://stackoverflow.com/questions/12964766/create-playlist-in-itunes-with-python-and-scripting-bridge

    p = {'name':'Testing', 'height': 100}
    s1 = {'name':'Slide1', 'height': 200}
    s2 = {'name':'Slide2', 'height': 300}

    # https://github.com/DominikPalo/scripting-bridge-definitions/blob/master/com.apple.iWork.Keynote/KeynoteScripting.swift
    # use these strings
    # https://stackoverflow.com/questions/12964766/create-playlist-in-itunes-with-python-and-scripting-bridge

    #doc = Keynote.classForScriptingClass_("document").alloc().initWithProperties_(p)
    doc = Keynote.classForScriptingClass_("document").alloc().initWithProperties_(p)
    slide1 = Keynote.classForScriptingClass_("slide").alloc().init()
    slide2 = Keynote.classForScriptingClass_("slide").alloc().init()

    Keynote.documents().insertObject_atIndex_(doc,0)

#    Keynote.documents().insertObject_atIndex_(doc,0)
    # You need to add it to an object otherwise is stays a future


    for d in Keynote.documents():

 
        # export theDoc to file outputPath as QuickTime movie using settings {image quality:best, slide duration:5}
        movType =  0x4b6d6f76
        imgType = 0x4d696d67
        fileName="export_dir"
        targetfile = NSURL.fileURLWithPath_(os.path.realpath(fileName))

       # https://stackoverflow.com/questions/3641426/restore-trash-item-using-scriptingbridge-in-mac-os-x-via-pyobjc
        # https://github.com/twardoch/keynote-slides-freezer/blob/main/keynote_slides_freezer/keynote_slides_freezer.py#L252
        """             doc.export(as_=k.slide_images, to=outpath, with_properties = {
                    k.export_style: k.IndividualSlides,
                    k.compression_factor: 0.9,
                    k.image_format: k.JPEG,
                    k.all_stages: not opts.skip_builds,
                    k.skipped_slides: False
                })
        """    
        jpegType = 0x4b69666a
        individualSlides =  0x4b707769
        print("exporting")
        d.slides().addObject_(slide1)
        d.slides().addObject_(slide2)
     #   d.exportTo_as_withProperties_(targetfile, imgType, {'exportStyle':individualSlides, 'compressionFactor':0.9, 'imageFormat':jpegType, 'allStages':True, 'skippedSlides':False})
#        d.exportTo_as_(fileName, movType)
       # d.iWorkItems().addObject_(slide1)
 
        # no effect
       # d.setValue_forKey_("my doc", "name")
        print("docu",d.name())

        for slide in d.slides():
            # no effect
           # slide.setValuesForKeysWithDictionary_({'name':'my slide'})
            t=(slide.defaultTitleItem())
            # Works !
            t.setValuesForKeysWithDictionary_({'objectText':'my title'})
            slideNr= slide.slideNumber()

            print("title",t.objectText().get()+str(slideNr))
            print("slide",slide.name())
            print("slide NR",slide.slideNumber())
            # Works
            slide.setValuesForKeysWithDictionary_({'presenterNotes':"my notes"})
            print(slide.presenterNotes().get())

            counter = 0 
            for item in slide.textItems():
                # Works !
                item.setValuesForKeysWithDictionary_({'objectText':'bla'+str(counter)})
                counter= counter+1
                print("text",item.objectText().get())
        keynoteFileFormat =  0x4b6e666
        # optional func saveIn(in_: AnyObject!, `as`: KeynoteSaveableFileFormat) // Save a document.
        # no eror , but not saving
        # is it for HFS ? or 
        #d.saveIn_as_("p.key",keynoteFileFormat)

   # Keynote.quitSaving_(0x6e6f2020)

def export_slide2():

    print(doc)
    print(slide1)
        
    #help(Keynote.documents())
 #   realdoc = Keynote.documents().insertObject_atIndex_(doc,0)
    Keynote.documents.addObject_(doc)
    print(doc.description)
    print(realdoc)
    realdoc = Keynote.documents()[0]

    realdoc.slides().addObject_(slide1)
    realdoc.slides().addObject_(slide2)

    realslide1 = realdoc.slides()[0]
    print(realslide1.name)

    realslide2 = realdoc.slides()[1]
    print(realslide2)

    for slide in realdoc.slides():
        print("SLide:",slide)

   # realdoc.slides().addObject_(slide1)
   # realdoc.slides().insertObject_atIndex_(slide2,0)
  #  print(realdoc)
  #  realslide1 = realdoc.slides()[0]
  #  realslide2 = realdoc.slides()[1]
   # realslide3 = realdoc.slides()[2]

   # realdoc.slides().addObject_(slide1)
   # realdoc.slides().addObject_(slide2)
    
   # print(slide1)
  #  print(realslide1)
  #  print(realslide2)
   # print(doc.height())
    #print(slide)
    #print(slide.height())
   # help(slide)

source = "demo.key"

#info_keynote(source)
#export_slide()
info_keynote("ls")