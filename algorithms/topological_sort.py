import unittest
from typing import List
from collections import defaultdict

class TopologicalSort(unittest.TestCase):
    def sort(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = set()
        arr = []
        for vertex in graph:
            if vertex not in visited and not self.dfs(vertex, graph, visited, arr, set()):
                return []

        return arr

    def dfs(self, vertex, graph, visited, arr, visiting) -> bool:
        visiting.add(vertex)
        if vertex in graph:
            for adj in graph[vertex]:
                if adj in visiting or (adj not in visited and not self.dfs(adj, graph, visited, arr, visiting)):
                    return False

        visiting.remove(vertex)
        visited.add(vertex)
        arr.append(vertex)

        return True

    def test_1(self):
        self.assertSequenceEqual(self.sort([[1, 0]]), [0, 1])

    def test_2(self):
        arr = self.sort([[1, 0], [2, 0], [3, 1], [3, 2]])
        self.assertTrue(all(x == y for x, y in zip(arr, [0, 1, 2, 3])) or all(x == y for x, y in zip(arr, [0, 2, 1, 3])))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
