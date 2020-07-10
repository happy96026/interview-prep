import unittest
from typing import List, Any
from collections import defaultdict
import math
import heapq

class Dijkstra(unittest.TestCase):
    def dijkstra(self, edges: List[List[Any]]) -> int:
        graph = defaultdict(list)
        for u, v, c in edges:
            graph[u].append([v, c])
            graph[v].append([u, c])

        visited = {}
        for vertex in graph:
            visited[vertex] = math.inf

        heap = [(0, 'a')]
        while heap:
            cost, vertex = heapq.heappop(heap)

            if cost < visited[vertex]:
                visited[vertex] = cost
                for v, c in graph[vertex]:
                    heapq.heappush(heap, (cost + c, v))

        return visited['c']

    def test_1(self):
        edges = [['a', 'd', 1], ['a', 'b', 6], ['d', 'b', 2], ['d', 'e', 1], ['b', 'e', 2], ['b', 'c', 5], ['e', 'c', 5]]
        self.assertEqual(self.dijkstra(edges), 7)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
