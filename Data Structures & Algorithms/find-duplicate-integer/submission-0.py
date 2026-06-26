class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        for n in d:
            if d[n] > 1:
                return n

            


