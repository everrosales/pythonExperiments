import copy

class Matrix:
	"""Class that add Matrix Support in python. """
 	def __init__(self, rows, columns, matrix= None):
 		self.columns = columns
 		self.rows = rows
 		if matrix != None:
 			self.matrix = matrix
 		else:
 			self.matrix = [[0 for x in range(columns)] for y in range(rows)]

 	def setItem(self, row, column, newValue):
 		self.matrix[row][column] = newValue

 	def setRow(self, rowIndex, list, fitMatrix= False):
 		if len(list) == self.columns:
 			self.matrix[rowIndex] = list
 		elif fitMatrix:
 			diffLen = len(list) - self.columns
 			if diffLen > 0:
 				for row in self.matrix:
 					for i in range(diffLen):
 						row.append(0)
 				self.columns = len(list)
 			else:
 				for i in range(diffLen):
 					list.append(0)
 			self.matrix[rowIndex] = list
 		else:
 			print "Row size does not fit the dimensions of the Matrix. "

 	def setColumn(self, columnIndex, list, fitMatrix= False):
 		if len(list) == self.rows:
 			for index in range(len(list)):
 				self.matrix[index][columnIndex] = list[index]
 		elif fitMatrix:
 			diffLen = len(list) - self.rows
 			if diffLen > 0:
 				for i in range(diffLen):
 					self.matrix.append([0 for i in range(self.columns)])
 				self.rows = len(list)
 			else:
 				for i in range(diffLen):
 					list.append(0)
 			for index in range(len(list)):
 				self.matrix[index][columnIndex] = list[index]
 		else:
 			print "Column size does not fit the dimensions of the Matrix. "

 	def getRow(self, rowIndex):
 		return self.matrix[rowIndex]

 	def getColumn(self, columnIndex):
 		newColumn = []
 		for row in self.matrix:
 			newColumn.append(row[columnIndex])
 		return newColumn

 	def lowerTriangular(self, storeLowerTri= False):
 		index = self.rows - 1
 		newMatrix = Matrix(self.rows, self.columns, self.matrix[:])
 		while index > -1:
 			newMatrix.matrix = self.reduceRowUp(index, newMatrix)
 			index -= 1
 		return newMatrix

 	def upperTriangular(self, storeUpperTri= False):
 		index = 0
 		newMatrix = Matrix(self.rows, self.columns, self.matrix[:])
 		while index < self.columns:
 			newMatrix.matrix = self.reduceRowDown(index, newMatrix)
 			index += 1
 		return newMatrix

 	def reduceRowUp(self, pivotRowIndex, currentMatrix):
 		for index in range(pivotRowIndex - 1, -1, -1):
 			currentMatrix.setRow(index, self.divideRowUp(pivotRowIndex, index, currentMatrix.matrix))
 		return currentMatrix.matrix

 	def reduceRowDown(self, pivotRowIndex, currentMatrix):
 		for index in range(pivotRowIndex + 1, self.rows):
 			currentMatrix.setRow(index, self.divideRowDown(pivotRowIndex, index, currentMatrix.matrix))
 		return currentMatrix.matrix

 	def divideRowUp(self, pivotRowIndex, targetRowIndex, matrix):
 		pivotRow = matrix[pivotRowIndex]
 		targetRow = matrix[targetRowIndex]
 		if pivotRow[pivotRowIndex] != 0:
 			diff = float(targetRow[pivotRowIndex])/float(pivotRow[pivotRowIndex])
 		else:
 			return targetRow
 		dividedRow = []
 		for itemIndex in range(len(targetRow) - 1, -1, -1):
 			newValue = round(((targetRow[itemIndex]) + pivotRow[itemIndex]*(-diff)), 5)
 			if newValue.is_integer():
 				newValue = int(newValue)
 			dividedRow = [newValue] + dividedRow
 		return dividedRow

 	def divideRowDown(self, pivotRowIndex, targetRowIndex, matrix):
 		pivotRow = matrix[pivotRowIndex]
 		targetRow = matrix[targetRowIndex]
 		if pivotRow[pivotRowIndex] != 0:
 			diff = float(targetRow[pivotRowIndex])/float(pivotRow[pivotRowIndex])
 		else:
 			return targetRow
 		dividedRow = []
 		for itemIndex in range(len(targetRow)):
 			newValue = round((targetRow[itemIndex] + pivotRow[itemIndex]*(-diff)), 5)
 			if newValue.is_integer():
 				newValue = int(newValue)
 			dividedRow.append(newValue)
 		return dividedRow

 	def normalizeRow(self, index, matrix):
 		targetRow = matrix.getRow(index)
 		newRow = []
 		if targetRow[index] == 0:
 			return targetRow
 		for item in targetRow:
 			newValue = float(item) / targetRow[index]
 			newRow.append(newValue)
 		return newRow

 	def normalizeColumn(self, index, matrix):
 		targetColumn = matrix.getColumn(index)
 		newColumn= []
 		if targetColumn[index] == 0:
 			return targetColumn
 		for item in targetColumn:
 			newValue = float(item) / targetColumn[index]
 			newColumn.append(newValue)
 		return newColumn

 	def normalize(self, vector):
 		newVector = []
 		targetVectorItems = vector.getColumn(0)
 		total = sum([item**2 for item in targetVectorItems])**.5
 		for item in targetVectorItems:
 			newVector.append(float(item)/total)
 		return Vector(vector.rows, newVector)

 	def rref(self, storeRref= False):
 		newMatrix = Matrix(self.rows, self.columns, self.matrix[:])
 		for rowIndex in range(min(newMatrix.rows, newMatrix.columns)):
 			newMatrix.setRow(rowIndex, self.normalizeRow(rowIndex, newMatrix))
 			newMatrix.matrix = self.reduceRowDown(rowIndex, newMatrix)
 		for rowIndex in range(min(newMatrix.rows, newMatrix.columns) - 1, -1, -1):
 			newMatrix.matrix = self.reduceRowUp(rowIndex, newMatrix)
 		return newMatrix

 	def determinant(self):
 		if self.columns == self.rows:
 			upperTri = self.upperTriangular()
 			det = 1
 			for index in range(self.rows):
 				det *= upperTri.matrix[index][index]
 			return det
 		else:
 			return "Matrix is not square. "

 	def transpose(self):
 		newMatrix = Matrix(self.columns, self.rows)
 		for rowIndex in range(len(self.matrix)):
 			for columnIndex in range(len(self.matrix[0])):
 				newMatrix.setItem(columnIndex, rowIndex, self.matrix[rowIndex][columnIndex])
 		return newMatrix

 	def projection(self, vectorOne, vectorTwo):
 		aTranspose = vectorOne.transpose()
 		top = ((aTranspose * vectorTwo))
 		bottom = ((aTranspose*vectorOne))
 		return Vector(1, [float(top.matrix[0][0])/bottom.matrix[0][0]]) * vectorOne

 	def orthogonal(self):
 		newMatrix = Matrix(self.rows, self.columns)
 		for index in range(self.columns):
 			projectionVector = Vector(self.rows, self.getColumn(index))
 			for projectionIndex in range(index):
				targetVector = Vector(self.rows, self.getColumn(projectionIndex))
				newProjectionVector = copy.copy(projectionVector)
 				newProjectionVector = newProjectionVector - self.projection(targetVector, projectionVector)
 			newProjectionVector = self.normalize(projectionVector)
 			newMatrix.setColumn(index, newProjectionVector.getColumn(0))
 		return newMatrix

 	def __str__(self):
 		string = ''
 		for row in self.matrix:
 			row = [str(x) for x in row]
 			string += ' '.join(row) + '\n'
 		return string

 	def __mul__(self, otherMatrix):
 		if (self.rows == self.columns == 1):
 			integer = self.matrix[0][0]
 			newMatrix = []
 			for rowIndex in range(otherMatrix.rows):
 				newRow = []
 				for columnIndex in range(otherMatrix.columns):
 					newRow.append((otherMatrix.matrix[rowIndex][columnIndex])*integer)
 				newMatrix.append(newRow)
 			return Matrix(otherMatrix.rows, otherMatrix.columns, otherMatrix)
 		elif self.columns != otherMatrix.rows:
 			return "These matrices can not be multiplied"
 		else:
 			newMatrix = []
 			for rowIndex in range(self.rows):
 				newRow = []
 				targetRow = self.matrix[rowIndex]
 				for columnIndex in range(otherMatrix.columns):
 					targetColumn = otherMatrix.getColumn(columnIndex)
 					newValue = 0
 					for itemIndex in range(otherMatrix.rows):
 						newValue += targetRow[itemIndex] * targetColumn[itemIndex]
 					newRow.append(newValue)
 				newMatrix.append(newRow)
 			return Matrix(self.rows, otherMatrix.columns, newMatrix)

 	def __div__(self, otherMatrix):
 		if self.rows == self.columns == 1:
 			integer = self.matrix[0][0]
 			newMatrix = []
 			for rowIndex in range(otherMatrix.rows):
 				newRow = []
 				for columnIndex in range(otherMatrix.columns):
 					newRow.append((otherMatrix.matrix[rowIndex][columnIndex])/integer)
 				newMatrix.append(newRow)
 			return Matrix(otherMatrix.rows, otherMatrix.columns, otherMatrix)
 		return "Matrix division is currently not supported"


 	def __add__(self, otherMatrix):
 		if self.rows != otherMatrix.rows or self.columns != otherMatrix.columns:
 			return "These Matrices can not be added."
 		else:
 			newMatrix = []
 			for rowIndex in range(self.rows):
 				newRow = []
 				leftRow = self.matrix[rowIndex]
 				rightRow = otherMatrix.matrix[rowIndex]
 				for itemIndex in range(self.columns):
 					newValue = leftRow[itemIndex] + rightRow[itemIndex]
 					newRow.append(newValue)
 				newMatrix.append(newRow)
 			return Matrix(self.rows, self.columns, newMatrix)

 	def __sub__(self, otherMatrix):
 		if self.rows != otherMatrix.rows or self.columns != otherMatrix.columns:
 			return "These Matrices can not be subtracted"
 		else:
 			newMatrix = []
 			for rowIndex in range(self.rows):
 				newRow = []
 				leftRow = self.matrix[rowIndex]
 				rightRow = otherMatrix.matrix[rowIndex]
 				for itemIndex in range(self.columns):
 					newValue = leftRow[itemIndex] - rightRow[itemIndex]
 					newRow.append(newValue)
 				newMatrix.append(newRow)
 			return Matrix(self.rows, self.columns, newMatrix)

class Identity(Matrix):
	def __init__(self, rows,  columns):
		self.rows = rows
		self.columns = columns
		self.matrix = [[0 for x in range(columns)] for y in range(rows)]
		for index in range(min(rows, columns)):
			self.setItem(index, index, 1)

class Vector(Matrix):
	def __init__(self, rows, vector):
		self.rows = rows
		self.columns = 1
		self.matrix = [[item] for item in vector]

	def __getitem__(self,index):
		return self.matrix[index]