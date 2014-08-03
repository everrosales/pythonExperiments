import unittest
from matrix import Matrix

class MatrixTests(unittest.TestCase):
	def setUp(self):
		self.matrix = Matrix(5,5)

	def testPrint(self):
		testMatrix = [[0,0,0,0,0] for i in range(5)]
		self.assertEqual(testMatrix, self.matrix.matrix)

	def testSetRow(self):
		self.matrix.setRow(1, [1,1,1,1,1])
		testMatrix = [[0,0,0,0,0] for i in range(5)]
		testMatrix[1] = [1,1,1,1,1]
		self.assertEqual(testMatrix, self.matrix.matrix)
		self.matrix.setRow(2, [1,1,1,1,1,1], True)
		testMatrix = [[0,0,0,0,0,0] for i in range(5)]
		testMatrix[1] = [1,1,1,1,1,0]
		testMatrix[2] = [1,1,1,1,1,1]
		print self.matrix
		self.assertEqual(testMatrix, self.matrix.matrix)

	def testSetColumn(self):
		self.matrix.setColumn(1, [1,1,1,1,1])
		testMatrix = [[0,1,0,0,0] for i in range(5)]
		self.assertEqual(testMatrix, self.matrix.matrix)
		self.matrix.setColumn(2,[1,1,1,1,1,1], True)
		testMatrix = [[0,1,1,0,0] for i in range(6)]
		testMatrix[5][1] = 0
		print self.matrix
		self.assertEqual(testMatrix, self.matrix.matrix)

if __name__ == '__main__':
	unittest.main()