# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# INORDER TRAVERSAL --> LEFT, ROOT, RIGHT
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def func(root):
            if not root:
                return []
            func(root.left)
            res.append(root.val)
            func(root.right)

        func(root)

        return res



