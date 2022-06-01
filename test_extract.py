from extract import extract
import unittest

class TestStringMethods(unittest.TestCase):
    # local testing
    def test_visualization(self):
        self.assertEqual(extract(),"Done")
if __name__=="__main__":
    unittest.main()