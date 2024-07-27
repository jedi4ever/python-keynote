from pykeynote import KeynoteApp
import os
import pytest

class TestKeynoteApp:


    @pytest.fixture
    def test_keynote_file(self):
        return os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'data','test.key'
        )
    
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

    def test_open_doc(self):
        FIXTURE_DIR = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'data','test.key'
        )
        keynote = KeynoteApp()
        keynote.open(FIXTURE_DIR)
        assert len(keynote.docs) > 0
        keynote.quit()

    def test_new_doc(self):
        keynote = KeynoteApp()
        existing_docs = len(keynote.docs)
        # Create a new doc
        new_doc = keynote.new_doc()
        # Now the number of docs should be one more
        assert existing_docs +1 == len(keynote.docs)
        # Close the doc
        new_doc.close()
        # Now the number of docs should be back to where it was
        assert existing_docs == len(keynote.docs)
        keynote.quit()