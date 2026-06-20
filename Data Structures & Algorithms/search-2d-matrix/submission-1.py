class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0
        mleft, mright = 0, len(matrix) - 1

        while mleft <= mright:
            count = (mleft + mright) // 2
            if matrix[count][-1] < target:
                mleft = count + 1
            elif matrix[count][-1] == target:
                return True
            elif matrix[count][-1] > target:
                nleft, nright = 0, len(matrix[count]) - 1
                while nleft <= nright:
                    mid = (nleft + nright) // 2
                    if matrix[count][mid] < target:
                        nleft = mid + 1
                    elif matrix[count][mid] > target:
                        nright = mid - 1
                    elif matrix[count][mid] == target:
                        return True
                mright = count - 1
        return False
                