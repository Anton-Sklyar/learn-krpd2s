import unittest
from src.MainProgram import MakeMatrix;

class MyTestCase(unittest.TestCase):
    def test_matrix(self):
        self.assertEqual(MakeMatrix('a',1,1), [[5]])

        self.assertEqual(MakeMatrix('b',2,2), [[5,6],
                                               [7,8]])

        self.assertEqual(MakeMatrix('x',3,3), [[1,2,3],
                                               [4,5,6],
                                               [7,8,9]])
    def test_value(self):
        self.assertRaises(ValueError,MakeMatrix,"X",0,-1)
        self.assertRaises(ValueError, MakeMatrix, "X", -1, 0)
        self.assertRaises(ValueError, MakeMatrix, "X", 0, 1)
        self.assertRaises(ValueError, MakeMatrix, "X", 1, 0)
        self.assertRaises(ValueError, MakeMatrix, "X", -1, 1)
        self.assertRaises(ValueError, MakeMatrix, "X", 1, -1)

    def test_types(self):
        self.assertRaises(TypeError, MakeMatrix, 1,'x',1.5)
        self.assertRaises(TypeError, MakeMatrix, True, 1,1)
        self.assertRaises(TypeError, MakeMatrix, 1, 1,1 )

if __name__ == '__main__':
    unittest.main()
