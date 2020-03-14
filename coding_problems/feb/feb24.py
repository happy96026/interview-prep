class Solution:
  def find_cycle(self, graph):
    not_visited = self.build_undirected_graph(graph)
    visited = set()
    stack = []
    
    while stack or not_visited:
      prev, popped = stack.pop() if stack else (None, not_visited.pop())

      if popped in visited:
        return True
      else:
        visited.add(popped)
        if popped in not_visited: not_visited.remove(popped)

        for vertex in graph[popped]:
          if vertex != prev:
            stack.append((popped, vertex))

    return False

  def build_undirected_graph(self, graph):
    not_visited = { key for key in graph }
    visited = set()
    stack = []

    while stack or not_visited:
      popped = stack.pop() if stack else not_visited.pop()

      if popped not in visited:
        visited.add(popped)
        if popped in not_visited: not_visited.remove(popped)

        for vertex in graph[popped]:
          graph[vertex] = graph[popped][vertex]
          graph[vertex][popped] = graph[popped]
          stack.append(vertex)

    return visited

def main():
  s = Solution()
  # graph = {
  #   'a': {},
  #   'a2': {},
  #   'a3': {},
  #   'b': {},
  #   'b2': {},
  #   'c': {},
  # }
  # graph['a']['a2'] = graph['a2']
  # graph['a']['a3'] = graph['a3']
  # graph['b']['b2'] = graph['b2']
  graph = {
    'a': { 'a2': {}, 'a3': {} },
    'b': { 'b2': {} },
    'c': {},
  }
  print(s.find_cycle(graph))
  graph['c'] = graph
  print(s.find_cycle(graph))

  graph = {
    'a': { 'b': {}, 'c': {} },
    'd': {}
  }
  graph['a']['b']['d'] = graph['d']
  graph['a']['c']['d'] = graph['d']
  print(s.find_cycle(graph))

if __name__ == '__main__':
  main()