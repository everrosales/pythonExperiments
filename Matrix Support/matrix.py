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
 		newMatrix = self.matrix[:]
 		while index > -1:
 			newMatrix = self.reduceRowUp(index, newMatrix)
 			index -= 1
 		return Matrix(len(newMatrix), len(newMatrix[0]), newMatrix)

 	def upperTriangular(self, storeUpperTri= False):
 		index = 0
 		newMatrix = self.matrix[:]
 		while index < self.columns:
 			newMatrix = self.reduceRowDown(index, newMatrix)
 			index += 1
 		return Matrix(len(newMatrix), len(newMatrix[0]), newMatrix)

 	def reduceRowUp(self, pivotRowIndex, currentMatrix):
 		for index in range(pivotRowIndex - 1, -1, -1):
 			currentMatrix[index] = self.divideRowUp(pivotRowIndex, index, currentMatrix)
 		return currentMatrix

 	def reduceRowDown(self, pivotRowIndex, currentMatrix):
 		for index in range(pivotRowIndex + 1, self.rows):
 			currentMatrix[index] = self.divideRowDown(pivotRowIndex, index, currentMatrix)
 		return currentMatrix

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
 		targetRow = matrix[index]
 		newRow = []
 		if targetRow[index] == 0:
 			return targetRow
 		for item in targetRow:
 			newValue = float(item) / targetRow[index]
 			newRow.append(newValue)
 		return newRow

 	def rref(self, storeRref= False):
 		newMatrix = self.matrix[:]
 		for rowIndex in range(min(len(newMatrix), len(newMatrix[0]))):
 			newMatrix[rowIndex] = self.normalizeRow(rowIndex, newMatrix)
 			newMatrix = self.reduceRowDown(rowIndex, newMatrix)
 		for rowIndex in range(min(len(newMatrix), len(newMatrix[0])) - 1, -1, -1):
 			newMatrix = self.reduceRowUp(rowIndex, newMatrix)
 		return Matrix(len(newMatrix), len(newMatrix[0]), newMatrix)

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
 		newMatrix = Matrix(self.rows, self.columns)
 		for rowIndex in range(len(self.matrix)):
 			for columnIndex in range(len(self.matrix[0])):
 				newMatrix.setItem(columnIndex, rowIndex, self.matrix[rowIndex][columnIndex])
 		return newMatrix

 	def __str__(self):
 		string = ''
 		for row in self.matrix:
 			row = [str(x) for x in row]
 			string += ' '.join(row) + '\n'
 		return string

 	def __mul__(self, otherMatrix):
 		if self.columns != otherMatrix.rows:
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

class Identity(Matrix):
	def __init__(self, rows,  columns):
		self.rows = rows
		self.columns = columns
		self.matrix = [[0 for x in range(columns)] for y in range(rows)]
		for index in range(min(rows, columns)):
			self.setItem(index, index, 1)