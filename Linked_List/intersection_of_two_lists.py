# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # calculate no of node in both linked list
        # take difference of both count
        # check check the condition and move the head accordingly
        h1 = headA
        h2 = headB
        c1 = 0
        c2 = 0
        while h1:
            c1 += 1
            h1 = h1.next

        while h2:
            c2 += 1
            h2 = h2.next

        d = abs(c1 - c2)
        h1 = headA
        h2 = headB
        if c1 > c2:
            while d:
                h1 = h1.next
                d -= 1
                c1 -= 1

        elif c2 > c1:
            while d:
                h2 = h2.next
                d -= 1
                c2 -= 1

        while h1 and h2:
            if h1 is h2:
                return h1

            h1 = h1.next
            h2 = h2.next

        return None




