import unittest
import abc

class SortTest(unittest.TestCase, abc.ABC):
    @abc.abstractmethod
    def sort(self, nums):
        pass

    def test_1(self):
        _input = []
        self.sort(_input)
        self.assertSequenceEqual(_input, sorted(_input))

    def test_2(self):
        _input = [2, 1]
        self.sort(_input)
        self.assertSequenceEqual(_input, sorted(_input))

    def test_3(self):
        _input = [1]
        self.sort(_input)
        self.assertSequenceEqual(_input, sorted(_input))

    def test_4(self):
        _input = [3, 5, 4]
        self.sort(_input)
        self.assertSequenceEqual(_input, sorted(_input))

    def test_5(self):
        _input = [-1, 2, -6, 3, 5, 123, 54, 2, -6, 23, 4]
        self.sort(_input)
        self.assertSequenceEqual(_input, sorted(_input))

class SelectionSort(SortTest):
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    def sort(self, nums):
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i + 1, len(nums)):
                min_index = min(j, min_index, key=lambda x: nums[x])
            nums[i], nums[min_index] = nums[min_index], nums[i]

class InsertionSort(SortTest):
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    def sort(self, nums):
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                else:
                    break

class BubbleSort(SortTest):
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    def sort(self, nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

class MergeSortTopDown(SortTest):
    def sort(self, nums):
        self.mergeSort(nums, 0, len(nums))

    def mergeSort(self, nums, lo, hi):
        if hi - lo > 1:
            mid = (lo + hi) // 2

            self.mergeSort(nums, lo, mid)
            self.mergeSort(nums, mid, hi)

            i, j = lo, mid
            arr = []
            while i < mid and j < hi:
                if nums[i] < nums[j]:
                    arr.append(nums[i])
                    i += 1
                else:
                    arr.append(nums[j])
                    j += 1
            while i < mid:
                arr.append(nums[i])
                i += 1
            while j < hi:
                arr.append(nums[j])
                j += 1

            nums[lo:hi] = arr

class MergeSortBottomUp(SortTest):
    def sort(self, nums):
        pass

class QuickSortLomuto(SortTest):
    def sort(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        pass

    def quickSort(self, nums, lo, hi):
        if lo < hi:
            pivot = self.partition(nums, lo, hi)
            self.quickSort(nums, lo, pivot - 1)
            self.quickSort(nums, pivot + 1, hi)

    def partition(self, nums, lo, hi):
        i = lo
        for j in range(lo, hi):
            if nums[j] < nums[hi]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[hi] = nums[hi], nums[i]

        return i

class QuickSortHoare(SortTest):
    def sort(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, lo, hi):
        if lo < hi:
            pivot = self.partition(nums, lo, hi)
            self.quickSort(nums, lo, pivot)
            self.quickSort(nums, pivot + 1, hi)

    def partition(self, nums, lo, hi):
        pivot = nums[(lo + hi) // 2]
        i = lo
        j = hi

        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

class HeapSort(SortTest):
    def sort(self, nums):
        '''
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        '''
        self.heapify(nums)
        for end in range(len(nums) - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.siftDown(nums, 0, end)

    def heapify(self, nums):
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        for start in range(len(nums) - 1, -1, -1):
            self.siftDown(nums, start, len(nums))
    
    def siftDown(self, nums, start, end):
        '''
        Time Complexity: O(log n)
        Space Complexity: O(1)
        '''
        root = swap = start
        left = 2*root + 1
        while left < end:
            if nums[swap] < nums[left]:
                swap = left
            if left + 1 < end and nums[swap] < nums[left + 1]:
                swap = left + 1
            
            if swap == root:
                return

            nums[root], nums[swap] = nums[swap], nums[root]
            root, left = swap, 2*swap + 1


def main():
    test_classes = [
        SelectionSort, 
        InsertionSort,
        BubbleSort,
        HeapSort, 
        MergeSortTopDown, 
        QuickSortLomuto, 
        QuickSortHoare
    ]
    tests = ['test_1', 'test_2', 'test_3', 'test_4', 'test_5']
    suite = unittest.TestSuite()
    for klass in test_classes:
        for test in tests:
            suite.addTest(klass(test))
    runner = unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    main()
