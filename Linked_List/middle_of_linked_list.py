# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        count1 = 0
        while temp:
            count += 1
            temp = temp.next

        mid = (count + 1) // 2
        if count % 2 == 0:
            mid = mid + 1

        temp1 = head
        while temp1:
            count1 += 1
            if count1 == mid:
                return temp1
            else:
                temp1 = temp1.next


##########   SLOW FAST POINTER APPROACH     ###########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
