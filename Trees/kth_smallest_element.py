# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.check = 0
        self.res = 0

        def func(root):
            if not root:
                return

            func(root.left)

            self.check += 1
            if self.check == k:
                self.res = root.val
                return

            if self.check < k:
                func(root.right)

        func(root)

        return self.res

