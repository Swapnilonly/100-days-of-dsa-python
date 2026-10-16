from typing import List


class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.total = [0] * (4 * n)
        self.squares = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def apply(self, node: int, left: int, right: int, value: int) -> None:
        length = right - left + 1
        self.squares[node] += (
            2 * value * self.total[node] + value * value * length
        )
        self.total[node] += value * length
        self.lazy[node] += value

    def push(self, node: int, left: int, right: int) -> None:
        if self.lazy[node] == 0 or left == right:
            return

        mid = (left + right) // 2
        value = self.lazy[node]

        self.apply(node * 2, left, mid, value)
        self.apply(node * 2 + 1, mid + 1, right, value)
        self.lazy[node] = 0

    def update(
        self, node: int, left: int, right: int,
        ql: int, qr: int
    ) -> None:
        if ql <= left and right <= qr:
            self.apply(node, left, right, 1)
            return

        self.push(node, left, right)
        mid = (left + right) // 2

        if ql <= mid:
            self.update(node * 2, left, mid, ql, qr)
        if qr > mid:
            self.update(node * 2 + 1, mid + 1, right, ql, qr)

        self.total[node] = (
            self.total[node * 2] + self.total[node * 2 + 1]
        )
        self.squares[node] = (
            self.squares[node * 2] + self.squares[node * 2 + 1]
        )

    def range_add(self, left: int, right: int) -> None:
        if left <= right:
            self.update(1, 0, self.n - 1, left, right)

    def sum_squares(self) -> int:
        return self.squares[1]


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        answer = 0

        for right, value in enumerate(nums):
            previous = last_seen.get(value, -1)
            tree.range_add(previous + 1, right)
            answer += tree.sum_squares()
            last_seen[value] = right

        return answer % (10**9 + 7)
