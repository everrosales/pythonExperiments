import unittest
from matrix import Matrix

class MatrixTests(unittest.TestCase):
	def setUp(self):
		self.matrix = Matrix(5,5)
		self.matrix3by3 = Matrix(3,3)
		self.matrix3by3.setRow(0, [1,2,3])
		self.matrix3by3.setRow(1, [1,5,1])
		self.matrix3by3.setRow(2, [1,0,2])

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
		self.assertEqual(testMatrix, self.matrix.matrix)

	def testSetColumn(self):
		self.matrix.setColumn(1, [1,1,1,1,1])
		testMatrix = [[0,1,0,0,0] for i in range(5)]
		self.assertEqual(testMatrix, self.matrix.matrix)
		self.matrix.setColumn(2,[1,1,1,1,1,1], True)
		testMatrix = [[0,1,1,0,0] for i in range(6)]
		testMatrix[5][1] = 0
		self.assertEqual(testMatrix, self.matrix.matrix)

	def testReduceRow(self):
		newMatrix = self.matrix3by3.reduceRow(0, self.matrix3by3.matrix)
		testMatrix = [[1, 2, 3], [0, 3, -2], [0, -2, -1]]
		self.assertEqual(testMatrix, newMatrix)

	def testUpperTriangular(self):
		testMatrix = [[1, 2, 3], [0, 3, -2], [0, 0, -2.33333]]
		self.assertEqual(testMatrix, self.matrix3by3.upperTriangular().matrix)
	
	def testDet(self):
		self.assertEqual(-6.99999, self.matrix3by3.determinant())

if __name__ == '__main__':
	unittest.main()