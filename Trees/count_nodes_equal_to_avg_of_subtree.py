# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def func(node):
            if not node:
                return 0, 0

            lsum, lcount = func(node.left)
            rsum, rcount = func(node.right)

            summ = (lsum + rsum + node.val)
            count = lcount + rcount + 1

            if summ // count == node.val:
                self.res += 1

            return summ, count

        func(root)

        return self.res


