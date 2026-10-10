# OPTIMAL SOLUTION

class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int,
    ) -> int:
        differences = [
            abs(a - b) for a, b in zip(nums1, nums2)
        ]
        operations = k1 + k2

        if sum(differences) <= operations:
            return 0

        left, right = 0, max(differences)

        while left < right:
            mid = (left + right) // 2

            required = sum(
                max(diff - mid, 0)
                for diff in differences
            )

            if required <= operations:
                right = mid
            else:
                left = mid + 1

        remaining = operations

        for index, diff in enumerate(differences):
            remaining -= max(diff - left, 0)
            differences[index] = min(diff, left)

        for index, diff in enumerate(differences):
            if remaining == 0:
                break

            if diff == left:
                differences[index] -= 1
                remaining -= 1

        return sum(diff * diff for diff in differences)