# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def helper(node, arr):
            if node.left == None and node.right == None:
                arr.append(node.val)
                return
            else:
                if node.left:
                    helper(node.left, arr)
                arr.append(node.val)
                if node.right:
                    helper(node.right, arr)
                return

        if root:
            helper(root, ans)
        return ans