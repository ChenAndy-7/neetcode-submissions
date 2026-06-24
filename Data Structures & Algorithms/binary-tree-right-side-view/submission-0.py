# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        res = []

        def helper(node, ans, level):
            if node is None:
                return []

            if len(ans) <= level:
                ans.append([])
            
            ans[level].append(node.val)

            helper(node.left, ans, level + 1)
            helper(node.right, ans, level + 1)

        helper(root, ans, 0)
        for i in range(len(ans)):
            res.append(ans[i][-1])

        return res




        

