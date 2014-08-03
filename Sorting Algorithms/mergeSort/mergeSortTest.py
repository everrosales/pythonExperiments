from mergeSort import MergeSort
import time
import random as rand
import unittest

class MergeSortTests(unittest.TestCase):
    """Unit testing class for MergeSort. """

    def setUp(self):
        testList = range(10000)
        rand.shuffle(testList)
        self.unsortedList = testList 
        
    def testInit(self):
        newList = self.unsortedList[:]
        mergeSort = MergeSort(newList)
        self.unsortedList.sort()
        self.assertEqual(str(self.unsortedList), str(mergeSort))

    def testIndex(self):
        newList = self.unsortedList[:]
        randInt = rand.choice(newList)
        mergeSort = MergeSort(newList)
        newList.sort()
        self.assertEqual(newList.index(randInt), mergeSort.index(randInt))
        self.assertEqual(-1, mergeSort.index(100001))

    def testContains(self):
        newList = self.unsortedList[:]
        randInt = rand.choice(newList)
        mergeSort = MergeSort(newList)
        self.assertEqual(True, mergeSort.contains(randInt))
        self.assertEqual(False, mergeSort.contains(10001))

if __name__ == '__main__':
    unittest.main()


