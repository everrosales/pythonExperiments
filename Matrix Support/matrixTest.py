import unittest
from matrix import *

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

	def testReduceRowDown(self):
		newMatrix = self.matrix3by3.reduceRowDown(0, self.matrix3by3.matrix)
		testMatrix = [[1, 2, 3], [0, 3, -2], [0, -2, -1]]
		self.assertEqual(testMatrix, newMatrix)

	def testReduceRowUp(self):
		newMatrix = self.matrix3by3.reduceRowUp(2, self.matrix3by3.matrix)
		testMatrix = [[-0.5, 2, 0], [0.5, 5, 0], [1, 0, 2]]
		self.assertEqual(testMatrix, newMatrix)

	def testUpperTriangular(self):
		testMatrix = [[1, 2, 3], [0, 3, -2], [0, 0, -2.33333]]
		self.assertEqual(testMatrix, self.matrix3by3.upperTriangular().matrix)

	def testLowerTriangular(self):
		testMatrix = [[-0.7, 0, 0], [0.5, 5, 0], [1, 0, 2]]
		self.assertEqual(testMatrix, self.matrix3by3.lowerTriangular().matrix)
	
	def testDet(self):
		self.assertEqual(-6.99999, self.matrix3by3.determinant())

	def testRref(self):
		testMatrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
		self.assertEqual(testMatrix, self.matrix3by3.rref().matrix)
		newMatrix3by4 = Matrix(3,4)
		newMatrix3by4.setRow(0, [1,2,1,2])
		newMatrix3by4.setRow(1, [2,1,1,2])
		newMatrix3by4.setRow(2, [3,2,3,2])
		testMatrix = [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1 ,-1]]
		self.assertEqual(testMatrix, newMatrix3by4.rref(newMatrix3by4.matrix).matrix)
		newMatrix4by3 = Matrix(4,3)
		newMatrix4by3.setColumn(0, [1,2,1,2])
		newMatrix4by3.setColumn(1, [2,1,1,2])
		newMatrix4by3.setColumn(2, [3,2,3,2])
		testMatrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		self.assertEqual(testMatrix, newMatrix4by3.rref(newMatrix4by3.matrix).matrix)

	def testMul(self):
		identityMatrix = Matrix(3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
		self.assertEqual(self.matrix3by3.matrix, (self.matrix3by3 * identityMatrix).matrix)
		testMatrix = Matrix(3, 3, [[1, 1, 1], [0, 1, 0], [0, 0, 1]])
		testGoal = [[1, 3, 4], [1, 6, 2], [1, 1, 3]]
		self.assertEqual(testGoal, (self.matrix3by3 * testMatrix).matrix)

	def testAdd(self):
		testGoal = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
		newMatrix = [[0, -1, -2], [1, -3, 1], [2, 3, 1]]
		addedMatrix = Matrix(3, 3, newMatrix)
		self.assertEqual(testGoal, (self.matrix3by3 + addedMatrix).matrix)
		error = "These Matrices can not be added."
		self.assertEqual(error, (self.matrix + addedMatrix))

	def testTranspose(self):
		targetGoal = [[1, 1, 1], [2, 5, 0], [3, 1, 2]]
		self.assertEqual(targetGoal, self.matrix3by3.transpose().matrix)

	def testIdentity(self):
		identity = Identity(3, 3)
		targetGoal = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
		self.assertEqual(targetGoal, identity.matrix)


if __name__ == '__main__':
	unittest.main()