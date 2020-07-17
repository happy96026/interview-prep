import unittest
from typing import List
from collections import defaultdict

class Solution(unittest.TestCase):
    def numConnectedComponents(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        vertices = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            vertices.add(u)
            vertices.add(v)

        visited = set()
        connected = 0
        for v in vertices:
            if v not in visited:
                connected += 1
                stack = [v]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        for adj in graph[node]:
                            stack.append(adj)

        return connected


    def test_1(self):
        self.assertEqual(self.numConnectedComponents([[1, 2], [2, 3], [4, 1], [5, 6]]), 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
