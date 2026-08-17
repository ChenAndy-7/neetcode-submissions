class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        m = defaultdict(int)

        for i in nums:
            m[i] += 1

        for j in m:
            if m[j] > 1:
                return True

        return False

