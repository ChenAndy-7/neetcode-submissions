class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1

        while n >= 0:
            n = n - rows
            if n >= 0:
                rows += 1
            else:
                return rows - 1

