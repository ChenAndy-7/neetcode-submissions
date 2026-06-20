import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort( arr, start, end):
            if start >= end:
                return

            pivot = partition(arr, start, end)
            quicksort(arr, start, pivot  - 1)
            quicksort(arr, pivot + 1, end)



        
        def partition( arr, start, end):
            rand = random.randint(start, end)
            arr[rand], arr[end] = arr[end], arr[rand]
            pivot = arr[end]

            i = start - 1
            

            for j in range(start, end):
                if arr[j] < pivot:
                    i += 1
                    arr[j], arr[i] = arr[i], arr[j]

            i += 1
            arr[end], arr[i] = arr[i], arr[end]
            return i

        quicksort(nums, 0, len(nums) -1)
        return nums
                    