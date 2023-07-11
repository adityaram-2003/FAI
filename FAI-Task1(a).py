import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in sorted(graph[vertex]):  # Sort the neighbours
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['D', 'F'],
             'C': ['G'],
             'D': ['E', 'G'],
             'E': [],
             'F': ['G'],
             'G': []
            }
    print("Following is Breadth First Traversal: ")
    bfs(graph, 'A')
