class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}

        for i in range(len(nums)):
            hs.update({nums[i]: i })

        for j in range(len(nums)):
            diff = target - nums[j]

            if diff in hs and hs.get(diff) != j:
                return sorted([hs.get(diff), j])