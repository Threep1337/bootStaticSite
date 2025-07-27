import unittest
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title,"Hello")

    def test_basic_title_withSpaces(self):
        title = extract_title("# Hello this is a long title")
        self.assertEqual(title,"Hello this is a long title")

    def test_basic_title_withTrailingSpaces(self):
        title = extract_title("# Hello this is a long title    ")
        self.assertEqual(title,"Hello this is a long title")



if __name__ == "__main__":
    unittest.main()
