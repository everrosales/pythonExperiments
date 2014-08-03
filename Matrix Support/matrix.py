class Matrix:
	"""Class that add Matrix Support in python. """
 	def __init__(self, rows, columns):
 		self.columns = columns
 		self.rows = rows
 		self.matrix = [[0 for x in range(columns)] for y in range(rows)]

 	def setItem(self, row, column, newValue):
 		self.matrix[row][column] = newValue

 	def setRow(self, rowIndex, list, extendMatrix= False):
 		if len(list) == self.columns:
 			self.matrix[rowIndex] = list
 		elif extendMatrix:
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

 	def setColumn(self, columnIndex, list, extendMatrix= False):
 		if len(list) == self.rows:
 			for index in range(len(list)):
 				self.matrix[index][columnIndex] = list[index]
 		elif extendMatrix:
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

 	def __str__(self):
 		string = ''
 		for row in self.matrix:
 			row = [str(x) for x in row]
 			string += ' '.join(row) + '\n'
 		return string
