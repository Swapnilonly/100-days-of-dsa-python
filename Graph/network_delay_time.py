from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(
        self,
        times: list[list[int]],
        n: int,
        k: int
    ) -> int:
        graph = defaultdict(list)

        for source, target, weight in times:
            graph[source].append((target, weight))

        distances = {node: float("inf") for node in range(1, n + 1)}
        distances[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if current_time > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = current_time + weight

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        max_time = max(distances.values())

        return -1 if max_time == float("inf") else max_time