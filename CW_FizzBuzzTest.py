import unittest
import CW_FizzBuzz as fb

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fb,"hello world!")

if __name__ == '__main__':
    unittest.main()