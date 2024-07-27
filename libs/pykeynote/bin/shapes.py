#!/usr/bin/env python

from pykeynote import KeynoteProcess, KeynoteApp

keynote_app = KeynoteApp()
keynote_app.activate()
keynote_process = KeynoteProcess()

keynote_process.add_rectangle()

keynote_window = keynote_process.windows[0]
#keynote_window.toggle_document()
keynote_window.toggle_sub()

#keynote_window.add_rectangle()
#keynote_window.add_rectangle()
#keynote_window.add_rectangle()
#keynote_window.add_rectangle()

