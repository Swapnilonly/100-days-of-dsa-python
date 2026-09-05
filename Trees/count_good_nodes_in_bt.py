# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def func(root, maxx):
            if not root:
                return

            if root.val >= maxx:
                self.count += 1
            maxx = max(maxx, root.val)

            func(root.left, maxx)
            func(root.right, maxx)

        func(root, root.val)

        return self.count

