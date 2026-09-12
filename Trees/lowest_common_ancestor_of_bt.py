class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def func(node):
            if not node:
                return None

            # If current node is p or q
            if node == p or node == q:
                return node

            left = func(node.left)
            right = func(node.right)

            # p and q found in different subtrees
            if left and right:
                return node

            # Return whichever node was found
            return left if left else right

        return func(root)