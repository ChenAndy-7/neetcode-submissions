class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()

        for i in nums:
            tracker.add(i)
        
        return len(tracker) != len(nums)