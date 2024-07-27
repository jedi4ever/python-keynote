#!/usr/bin/env python
from pykeynote import KeynoteProcess

def dump_elements(element, level):
    ui_elements = element.UI_elements
   #print(ui_elements)
    if (ui_elements is not None):
        elements=ui_elements.get()
        prefix = level * "-"

        for element in elements:
            print(prefix+">", element.properties.get())
            actions = element.actions.get()
            for action in actions:
                print(prefix+"> [action]", action.get().properties.get())
            attributes = element.attributes.get()
            for attribute in attributes:
                print(prefix+"> [attribute]", attribute.get().properties.get())
            dump_elements(element,level+1)

keynote_process = KeynoteProcess()
keynote_window = keynote_process.windows[0]
dump_elements(keynote_window._window, 0)