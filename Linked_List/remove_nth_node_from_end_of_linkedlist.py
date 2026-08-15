class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        head1 = head

        # Count nodes
        while head1:
            count += 1
            head1 = head1.next

        # If head itself needs to be removed
        if count == n:
            return head.next

        # Find the node before the target node
        target = count - n
        head2 = head

        while head2:
            target -= 1

            if target == 0:
                break

            head2 = head2.next

        # Remove target node
        head2.next = head2.next.next

        return head