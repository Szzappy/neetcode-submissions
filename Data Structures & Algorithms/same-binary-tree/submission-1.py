# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True

        def check_same(p, q):
            nonlocal same
            if p is None and q is None:
                return 

            try:
                check_same(p.left, q.left)
                check_same(p.right, q.right)

                if p.val != q.val:
                    same = False
            except:
                same = False


        check_same(p, q)
        return same