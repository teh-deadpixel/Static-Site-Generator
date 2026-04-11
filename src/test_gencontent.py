import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_happy_flow(self):
        title = extract_title("# Hello\nohio")
        self.assertEqual(title, "Hello")
    
    def test_no_header(self):
        title = ("##this will work\n\n-i will be a backend dev")
        with self.assertRaises(Exception):
            extract_title(title)
    
    def test_extra_whitespace(self):
        title = extract_title("#  hello ")
        self.assertEqual(title, "hello")

if __name__ == "__main__":
    unittest.main()