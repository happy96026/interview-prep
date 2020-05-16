from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

class Solution:
    def reverseGraph(self, graph):
        d = defaultdict(list)

        for node in graph.values():
            for adj in node.adjacent:
                d[adj].append(node)

        for node in graph.values():
            node.adjacent = d[node]

        return graph


def main():
    s = Solution()
    
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.adjacent += [b, c]
    b.adjacent += [c]

    graph = {
        a.value: a,
        b.value: b,
        c.value: c
    }

    for _, val in s.reverseGraph(graph).items():
        print(val.value, [v.value for v in val.adjacent])

if __name__ == '__main__':
    main()