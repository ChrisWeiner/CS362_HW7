#Christopher Weiner
#CS326 - HW7
#LeapYear Testing
import CW_LeapYear as LP
import unittest

class TestCase1(unittest.TestCase):
    def test1(self):
        self.assertEqual(LP,"2000 is a leap year")

if __name__ == "__main__":
    unittest.main()