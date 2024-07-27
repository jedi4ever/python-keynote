from pykeynote.keynote_app import KeynoteApp

class TestKeynoteApp:
    def test_my_name(self):
        my_name = "Patrick Debois"
        assert my_name == "Patrick Debois"

    def test_themes(self):
        keynote = KeynoteApp()
        assert len(keynote.themes) > 0

    def test_version(self):
        keynote = KeynoteApp()
        version = keynote.version
        # the version is a string
        assert isinstance(version, str)
        # the version should at least contain 1 dot
        assert "." in version
