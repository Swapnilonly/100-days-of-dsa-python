# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# POST ORDER TRAVERSAL  --> LEFT, RIGHT, ROOT
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def func(root):
            if not root:
                return []

            func(root.left)
            func(root.right)
            res.append(root.val)

        func(root)

        return res
