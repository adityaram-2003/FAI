# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
graph = {'A': set(['B', 'C']),
         'B': set(['D', 'F']),
         'C': set(['G']),
         'D': set(['E','G']),
         'E': set([]),
         'F': set(['G']),
         'G': set([])
        }
dfs(graph, 'B')
