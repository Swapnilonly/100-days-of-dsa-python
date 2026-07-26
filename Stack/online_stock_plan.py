class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # check top of stack is less than current price
        # if yes ---> icrement the span and append (pirce, span)
        # the increment of span will be decided based span of stacks top element
        # if no ---> pop the top element
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            cspan = self.stack[-1][1]
            span = cspan + span
            self.stack.pop()

        self.stack.append((price, span))
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)