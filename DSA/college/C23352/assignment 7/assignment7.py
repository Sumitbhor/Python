from collections import deque 
# Sample locations and routes
locations = ['A', 'B', 'C', 'D', 'E']

# Adjacency matrix for DFS
adj_matrix = [
    [0, 1, 1, 0, 0],  # A
    [1, 0, 1, 1, 0],  # B
    [1, 1, 0, 0, 1],  # C
    [0, 1, 0, 0, 1],  # D
    [0, 0, 1, 1, 0]   # E
]

# Adjacency list for BFS
adj_list = {
    'A': ['B','C'],
    'B': ['A','C','D'],
    'C': ['A','B','E'],
    'D': ['B','E'],
    'E': ['C','D']
}

# DFS using adjacency matrix
def dfs(start):
    visited = [False]*len(locations)
    result = []
    stack = [locations.index(start)]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(locations[node])
            # Add neighbors in reverse order to maintain proper visiting order
            for i in reversed(range(len(locations))):
                if adj_matrix[node][i] == 1 and not visited[i]:
                    stack.append(i)
    return result

# BFS using adjacency list
def bfs(start):
    visited = {loc: False for loc in locations}
    result = []
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result

# Perform traversals starting from 'A'
print("DFS Sequence:", dfs('A'))
print("BFS Sequence:", bfs('A'))
