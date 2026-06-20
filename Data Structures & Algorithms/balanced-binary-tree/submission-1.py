# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def helper(root, valid):
            if root is None:
                return 0

            if self.valid == False:
                return 0

            left = helper(root.left, valid)
            right = helper(root.right, valid)

            

            if abs(left - right) > 1:
                self.valid = False
            return max(left, right) + 1 

        helper(root, self.valid)
        return self.valid