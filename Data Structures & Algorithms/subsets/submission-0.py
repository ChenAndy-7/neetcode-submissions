class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(start_idx, path):
            ans.append(path[:])
            

            for i in range(start_idx, len(nums)):
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()

            
        helper(0, [])
        return ans