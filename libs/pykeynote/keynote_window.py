import appscript
#from pykeynote.keynote_process import KeynoteProcess

class KeynoteWindow:
    def __init__(self,window):
        self._window = window

    def toggle_format(self):
        self._window.toolbars[0].groups[0].radio_buttons[0].click()

    def toggle_animate(self):
        self._window.toolbars[0].groups[0].radio_buttons[1].click()

    def toggle_document(self):
        k = appscript.k
        # 1 = Format
        # 2 = Animate
        # 3 = Document
        properties = self._window.toolbars[0].groups[0].radio_buttons[0].properties.get()
        print("desc",properties[k.description])
        # value = 0 (not visible), 1 = (visible)
        print("selected",properties[k.value])
        for p in properties:
            print("property",p)
        self._window.toolbars[0].groups[0].radio_buttons[1].click()

    def toggle_sub(self):
        k = appscript.k
        # 1 = Style
        # 2 = Text
        # 3 = Arrange 
        #self._window.radio_groups[1].radio_buttons[1].click()
        
        # First color well
        #self._window.scroll_areas[1].color_wells[1].click()

        # when the color well is open, set the colors
        print(appscript.app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields['Red'].value.set("0"))
        print(appscript.app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields['Green'].value.set("0"))
#        print(appscript.app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields['Blue'].selected.set(True))
        print(appscript.app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields['Blue'].value.set("255"))

        # Needs a confirm (alternative is to send a keystroke)
        appscript.app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields['Blue'].actions['AXConfirm'].perform()


        # Try enter or action "AXConfirm"
        # https://www.macscripter.net/t/set-value-of-text-field/75926/8
        #appscript.app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields['Blue'].
        #                                perform action "AXConfirm"
        #       needs enter for it to take effect

       # appscript.app('System Events').application_processes['Keynote'].windows[2].splitter_groups[1].text_fields[1].selected.set(True)
        #app('System Events').application_processes['Keynote'].windows['Color Fill'].splitter_groups[1].text_fields[1].keystroke('99')

