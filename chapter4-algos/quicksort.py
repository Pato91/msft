import unittest

def quicksort(arr, low, high):
    '''quicksort
    use last element as a pivot
    arr: array to be sorted
    low: lowest index in array, default = 0
    high: last index in array: len(arr) -1

    Runtime: 0(nlogn) worst case, O(nlogn) best case
    '''
    def partition(arr, low, high):
        ''' core function to return the index of pivot after partitioning '''
        pivot = arr[high]
        i = low-1 #start at negative position, track index of smaller elements
        for j in range(low, high):
            if arr[j] <= pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = pivot, arr[i+1] # move pivot to center
        return i+1

    if low < high:
        p = partition(arr, low, high) #index of pivot after partitioning

        quicksort(arr, low, p-1) #sort lower side of p
        quicksort(arr, p+1, high) #sort upper side of p

    return arr

class Test(unittest.TestCase):
    def test_worst_case(self):
        self.assertEqual( quicksort([1,2,3,4,5,6,7], 0, 6), [1,2,3,4,5,6,7] )

    def test_sort(self):
        self.assertEqual( quicksort([7,3,1,5,2,6,4], 0, 6), [1,2,3,4,5,6,7] )

if __name__ == '__main__':
    unittest.main()
