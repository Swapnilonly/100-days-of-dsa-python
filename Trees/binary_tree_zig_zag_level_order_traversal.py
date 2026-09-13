# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res1 = []
        r_l = False

        while queue:
            level = len(queue)
            res = []
            for _ in range(level):
                node = queue.popleft()
                res.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if r_l:
                res.reverse()

            res1.append(res)
            r_l = not r_l

        return res1
