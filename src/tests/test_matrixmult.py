import unittest
from src.MainProgram import MatrixMult;

class MyTestCase(unittest.TestCase):
    def test_matrix(self):
        self.assertEqual(MatrixMult([[1,2],[2,2]],[[1, 1], [2, 2]],2,2,2), [[5, 6], [5, 6]])
        self.assertEqual(MatrixMult([[3, 4]],[[5], [6]],1,1,2), [[39]])
        self.assertEqual(MatrixMult([[60]], [[2]], 1, 1, 1), [[120]])

    def test_value(self):
        self.assertRaises(ValueError,MatrixMult,[[]], [[]],0,1,-1)
        self.assertRaises(ValueError, MatrixMult,[[]], [[]], 1, 0,-1)
        self.assertRaises(ValueError, MatrixMult, [[]], [[]], -1, 1, 0)

    def test_types(self):
        self.assertRaises(TypeError, MatrixMult, [[]], [[]],1,1,'')
        self.assertRaises(TypeError, MatrixMult, [[]], [[]], 1, '', True)
        self.assertRaises(TypeError, MatrixMult, [[]], [[]], False, 1,1 )
        self.assertRaises(TypeError, MatrixMult, [[]], 1, 1, 1, 1)
        self.assertRaises(TypeError, MatrixMult, 1.1, [[]], 1, 1, 1)
        self.assertRaises(TypeError, MatrixMult, [], [[]], 1, 1, 1)
        self.assertRaises(TypeError, MatrixMult, [[]], [], 1, 1, 1)

if __name__ == '__main__':
    unittest.main()
