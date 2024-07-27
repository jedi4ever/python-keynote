import os
from pykeynote import KeynoteApp
import pytest


class TestKeynoteDoc:

    @pytest.fixture
    def test_keynote_file(self):
        return os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'data','test.key'
        )

    def test_layouts(self, test_keynote_file):
      
        keynote = KeynoteApp()
        keynote.open(test_keynote_file)
        doc = keynote.docs[0]
        # The test.key file has more then 1 layout
        assert len(doc.layouts) > 0
        doc.close()

    def test_slides_count(self, test_keynote_file):

        keynote = KeynoteApp()
        keynote.open(test_keynote_file)
        doc = keynote.docs[0]
        # The test.key file has 2 slides
        assert len(doc.slides) == 2
        doc.close()