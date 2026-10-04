from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            current_prices = prices.copy()

            for from_city, to_city, price in flights:
                if prices[from_city] == float("inf"):
                    continue

                new_price = prices[from_city] + price

                if new_price < current_prices[to_city]:
                    current_prices[to_city] = new_price

            prices = current_prices

        return -1 if prices[dst] == float("inf") else prices[dst]