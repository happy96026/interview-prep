from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        visited = [-1] * numCourses
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        for node in range(numCourses):
            if visited[node] == -1 and not self.dfs(node, visited, graph, result):
                return []
        
        return result

    # Recursive Solution
    def dfs(self, u, visited, graph, result):
        if visited[u] == 0:
            return False
        elif visited[u] == 1:
            return True

        visited[u] = 0
        for v in graph[u]:
            if not self.dfs(v, visited, graph, result):
                return False

        result.append(u)
        visited[u] = 1

        return True

    # Iterative Solution
    # def dfs(self, node, visited, graph):
    #     stack = [(node, 0)]
    #     result = []
    #     while stack:
    #         u, val = stack.pop()
    #         if val == 0:
    #             if visited[u] == -1:
    #                 visited[u] = val
    #                 stack.append((u, 1))
    #                 for v in graph[u]:
    #                     stack.append((v, 0))
    #             elif visited[u] == 0:
    #                 return []
    #         else:
    #             visited[u] = val
    #             result.append(u)

    #     return result

            
def main():
    s = Solution()
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

if __name__ == '__main__':
    main()