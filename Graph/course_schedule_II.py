from collections import deque


class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: list[list[int]]
    ) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque(
            course for course in range(numCourses)
            if indegree[course] == 0
        )

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        if len(order) != numCourses:
            return []

        return order