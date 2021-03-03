#Christopher Weiner
#CS326 - HW7
#LeapYear Testing
import CW_LeapYear as LP
import unittest

class TestCase1(unittest.TestCase):
    def test1(self):
        self.assertEqual(LP.LeapYear(2000),"2000 is a leap year")
    def test2(self):
        self.assertEqual(LP.LeapYear(1700),"1700 is not a leap year")

if __name__ == "__main__":
    unittest.main()