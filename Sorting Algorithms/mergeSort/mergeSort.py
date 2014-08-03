class MergeSort:
	""" O(N log N) sorting class."""
	def __init__(self, list):
		"""Sorts List upon initializing instance of class. """
		self.list = self.sort(list)

	def merge(self, left, right):
		"""Merge function for merge sort. """
		joinedList = []
		leftIndex, rightIndex = 0, 0
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
		"""Recursive sorting and merge when len(list) == 1. """
		if list == None:
			list = self.list
		if len(list) == 1:
			return list
		midPoint = len(list)/2
		listLeft = self.sort(list[:midPoint])
		listRight = self.sort(list[midPoint:])
		return self.merge(listLeft, listRight)

	def index(self, target, sortedList= None):
		"""Indexing function for sorted list. O(Log N) """
		if sortedList == None:
			targetList = self.list
			return  self.findTarget(0, len(targetList), target, targetList) 
		return self.findTarget(0, len(sortedList), target, sortedList)

	def findTarget(self, leftIndex, rightIndex, target, sortedList):
		"""Helper function for index. """
		midPoint = (rightIndex + leftIndex)/2
		midValue = sortedList[midPoint]
		if rightIndex - leftIndex == 3:
			if midValue == target:
				return midPoint
			elif sortedList[midPoint + 1] == target:
				return midPoint + 1
			else:
				return -1
		elif target > midValue:
			return self.findTarget(midPoint, rightIndex, target, sortedList)
		elif target < midValue:
			return self.findTarget(leftIndex, midPoint, target, sortedList)
		else:
			return midPoint

	def contains(self, target, sortedList= None):
		"""Returns a boolean indicating if target is in list.
			Makes use of self.index(). O(Log N) 
			"""
		if sortedList == None:
			sortedList = self.list
		return self.findTarget(0, len(sortedList), target, sortedList) > -1

	def __str__(self):
		return str(self.list)

	def __getitem__(self, index):
		return self.list[index]