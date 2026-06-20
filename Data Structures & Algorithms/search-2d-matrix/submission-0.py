class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0

        while matrix[count][-1] < target and count < len(matrix) - 1:
            count += 1
        
        left, right = 0, len(matrix[count]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[count][mid] < target:
                left = mid + 1
            elif matrix[count][mid] > target:
                right = mid - 1
            elif matrix[count][mid] == target:
                return True
        
        return False