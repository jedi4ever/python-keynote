import appscript

from pykeynote.keynote_doc import KeynoteDoc
from pykeynote.keynote_theme import KeynoteTheme

class KeynoteApp:

    def __init__(self):
        keynote = appscript.app('Keynote')
        self._keynote = keynote

    def get_docs(self):
        docs = []
        for d in self._keynote.documents.get():
            docs.append(KeynoteDoc(d))
        return docs
    
    def get_version(self):
        return self._keynote.version.get()

    def get_themes(self):
        themes=[]
        for t in self._keynote.themes.get():
            themes.append(KeynoteTheme(t))
        return themes

    def new_doc(self):
        doc = self._keynote.make(new=appscript.k.document,with_properties={
    #        k.document_theme :my_theme,
    #        k.width: 1024,
    #        k.height: 768
        })
        return KeynoteDoc(doc)

    def quit(self):
        k = appscript.k
        # k.no , k.ask , k.ye

        # This just quits without saving
        # self._keynote.quit(saving=k.no)

        # This actually closes
        self._keynote.documents.close(saving=k.no)

    def activate(self):
        self._keynote.activate()

    def open(self,filename):
        self._keynote.activate()
        self._keynote.open(appscript.mactypes.File(filename))

    docs = property(get_docs)
    themes = property(get_themes)
    version = property(get_version)