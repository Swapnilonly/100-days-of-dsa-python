class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list
        second = slow.next
        slow.next = None

        # 3. Reverse second half
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        second = prev

        # 4. Merge both halves
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next