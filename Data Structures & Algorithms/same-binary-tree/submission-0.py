# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        if (p is None and q is not None) or (q is None and p is not None):
            return False
            
        def tree_to_list(root, lst):
            if root is None:
                lst.append(None)
                return

            left = tree_to_list(root.left, lst)
            right = tree_to_list(root.right, lst)

            lst.append(root.val)
            return

        tree_to_list(p, l1)
        tree_to_list(q, l2)
        return l1 == l2

