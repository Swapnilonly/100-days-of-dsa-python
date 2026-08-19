class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        count = 0
        slow = head
        fast = head
        curr = head

        # Count nodes
        while curr:
            count += 1
            curr = curr.next

        # Find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Skip middle node for odd-length list
        if count % 2 != 0:
            slow = slow.next

        # Reverse second half
        prev = None

        while slow:
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front

        # Compare first half and reversed second half
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True