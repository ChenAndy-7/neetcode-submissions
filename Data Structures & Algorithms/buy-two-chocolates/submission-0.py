class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        i, j = float('inf'), float('inf')


        for n in prices: 
            if n < j:
                if n < i:
                    j = i
                    i = n
                else:
                    j = n

        if (i + j > money):
            return money
        else:
            return money - (i + j)
