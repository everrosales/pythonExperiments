class SpeedSort:
	""" O(N log N) sorting class."""
	def __init__(self, list, sort= True):
		if sort:
			self.list = self.sort(list)
		else:
			self.list = list

	def join(self, left, right):
		joinedList = []
		leftIndex = 0
		rightIndex = 0
		while leftIndex < len(left) and rightIndex < len(right):
			if left[leftIndex] < right[rightIndex]:
				joinedList.append(left[leftIndex])
				leftIndex += 1
			else:
				joinedList.append(right[rightIndex])
				rightIndex += 1
		while leftIndex < len(left):
			joinedList.append(left[leftIndex])
			leftIndex += 1
		while rightIndex < len(right):
			joinedList.append(right[rightIndex])
			rightIndex += 1
		return  joinedList

	def sort(self, list= None):
		if list == None:
			list = self.list
		if len(list) == 1:
			return list
		midPoint = len(list)/2
		listLeft = self.sort(list[:midPoint])
		listRight = self.sort(list[midPoint:])
		return self.join(listLeft, listRight)

	def sortAndFindIndex(self, target):
		return self.list, self.findTarget(0, len(self.list), target)

	def findTarget(self, leftIndex, rightIndex, target, list= None):
		if list == None:
			list = self.list
		midPoint = (rightIndex + leftIndex)/2
		if list[midPoint] == target:
			return midPoint
		elif len(list) == 1:
			return -1
		elif list[midPoint] > target:
			return self.findTarget(midPoint, rightIndex, target, list)
		elif list[midPoint] < target:
			return self.findTarget(leftIndex, midPoint, target, list)

	def contains(self, target, list= None):
		if list == None:
			list = self.list
		sortedList = self.sort(list)
		return self.findTarget(0, len(list), target) > -1

	def __str__(self):
		return str(self.list)

list = [1,9,2,7,4,10]
speedSort = SpeedSort(list, False)
print speedSort
print speedSort.sort()
print speedSort.sortAndFindIndex(9)

