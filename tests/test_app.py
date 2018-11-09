import sys
sys.path.append('..')
import unittest

from app.sniff import Sniff

res = Sniff("url")

class TestApp(unittest.TestCase):
    def setUp(self):
        pass

    def test_tokenize_words(self):
        """ testing splitting sentences into words """
        self.assertEqual(res.tokenize_words("am going home"), ["am", "going", "home"])

    def test_remove_stop_words(self):
        """ testing removing stop words """
        self.assertEqual(res.remove_stop_words(["am", "going", "home"]), ["going", "home"])

if __name__ == "__main__":
    unittest.main()