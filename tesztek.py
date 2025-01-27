import unittest
from fuggvenyek import Muveletek

class TestMuveletek(unittest.TestCase):
    def setUp(self):
        self.math = Muveletek()

    def test_add(self):
        self.assertEqual(self.math.add(2,3),5)
        self.assertEqual(self.math.add(-1,1),0)

    def test_substact(self):
        self.assertEqual(self.math.substract(5,3),2)
        self.assertEqual(self.math.substract(0,5),-5)

    def test_multiply(self):
        self.assertEqual(self.math.multiply(4,3),12)
        self.assertEqual(self.math.multiply(-1,3),-3)

    def test_divide(self):
        self.assertEqual(self.math.divide(10,2),5)
        with self.assertRaises(ValueError):
            self.math.divide(10,0)

if __name__ == "__main__":
    unittest.main()
    