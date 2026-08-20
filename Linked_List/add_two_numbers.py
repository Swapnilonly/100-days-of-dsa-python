# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = 0
        prev = None
        dummy = ListNode()
        curr = dummy
        while temp1 or temp2:
            # exracting the num1 and num2
            num1 = temp1.val if temp1 else 0
            num2 = temp2.val if temp2 else 0
            # adding sum with carry
            summ = num1 + num2 + carry
            res = summ % 10
            carry = summ // 10

            # creating new node of list and adding value
            h = ListNode()
            h.val = res
            curr.next = h
            curr = curr.next
            # updating temp1 and temp2 by checking them
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        # checking if carry is left after all elements added
        if carry > 0:
            h = ListNode()
            h.val = carry
            curr.next = h
            curr = curr.next

        # returning the head of current summ of list
        return dummy.next


