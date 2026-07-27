# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtree = False

        def check_same(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return check_same(p.left, q.left) and check_same(p.right, q.right)

        def check_subtree(root):
            if root is None:
                return False

            if check_same(root, subRoot):
                return True

            return check_subtree(root.left) or check_subtree(root.right)
            
        return check_subtree(root)

            
                