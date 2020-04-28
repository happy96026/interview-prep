class Solution:
    def chainedWords(self, words):
        if not words:
            return False

        graph = {}
        for word in words:
            for i in (0, -1):
                graph[word[i]] = graph.get(word[i], { 'indegree': 0, 'edges': [] })

            graph[word[0]]['edges'].append(word[-1])
            graph[word[-1]]['indegree'] += 1

        stack = [words[0][0]]
        visited = set()
        while stack:
            char = stack.pop()
            if char not in visited:
                visited.add(char)
                for adj in graph[char]['edges']:
                    stack.append(adj)
        
        if len(visited) != len(graph):
            return False
        
        for char in graph:
            if graph[char]['indegree'] != len(graph[char]['edges']):
                return False
            
        return True
        

def main():
    s = Solution()
    print(s.chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
    print(s.chainedWords(['geek', 'king']))
    print(s.chainedWords(['for', 'geek', 'rig', 'kaf']))
    print(s.chainedWords(['aab', 'bac', 'aaa', 'cda']))
    print(s.chainedWords(['aaa', 'bbb', 'baa', 'aab']))
    print(s.chainedWords(['aaa']))
    print(s.chainedWords(['aaa', 'bbb']))
    print(s.chainedWords(['abc', 'efg', 'cde', 'ghi', 'ija']))
    print(s.chainedWords(['ijk', 'kji', 'abc', 'cba']))
    print(s.chainedWords(['axb', 'bxc', 'cxd', 'dxa', 'dxe', 'exd']))

if __name__ == '__main__':
    main()