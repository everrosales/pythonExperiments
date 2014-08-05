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

 	def upperTriangular(self, storeUpperTri= False):
 		index = 0
 		newMatrix = self.matrix[:]
 		while index < self.columns:
 			newMatrix = self.reduceRow(index, newMatrix)
 			index += 1
 		return Matrix(len(newMatrix), len(newMatrix[0]), newMatrix)

 	def reduceRow(self, pivotRowIndex, currentMatrix):
 		for index in range(pivotRowIndex + 1, self.rows):
 			currentMatrix[index] = self.divideRow(pivotRowIndex, index, currentMatrix)
 		return currentMatrix

 	def divideRow(self, pivotRowIndex, targetRowIndex, matrix):
 		pivotRow = matrix[pivotRowIndex]
 		targetRow = matrix[targetRowIndex]
 		if targetRow[pivotRowIndex] != 0:
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

 	def determinant(self):
 		if self.columns == self.rows:
 			upperTri = self.upperTriangular()
 			det = 1
 			for index in range(self.rows):
 				det *= upperTri.matrix[index][index]
 			return det

 		else:
 			return "Matrix is not square. "

 	def __str__(self):
 		string = ''
 		for row in self.matrix:
 			row = [str(x) for x in row]
 			string += ' '.join(row) + '\n'
 		return string