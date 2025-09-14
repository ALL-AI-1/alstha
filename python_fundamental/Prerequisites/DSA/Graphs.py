# Graph representations and traversals: adjacency list, adjacency matrix, BFS, DFS
# My code
from collections import defaultdict

# Adjacency list with repeated numbers (self-loops and multiple edges)
lst = [
    [0, 1], [0, 0], [0, 1], [1, 2], [1, 1], [1, 2], [2, 3], [2, 2], [2, 3],
    [3, 4], [3, 3], [3, 4], [4, 5], [4, 4], [4, 5], [5, 6], [5, 5], [5, 6],
    [6, 7], [6, 6], [6, 7], [7, 8], [7, 7], [7, 8], [8, 9], [8, 8], [8, 9],
    [9, 10], [9, 9], [9, 10]
]

Dd = defaultdict(list)

for u, v in lst:
    if v not in Dd[u]:
        Dd[u].append(v)

print(dict(Dd))


BFS="follow Queue [FIFO]" "Level By Level Search"
DFS="follow Stack [LIFO] or Recursion " "IN DEPTH SEARCH"
VERTICES="Node ->the element"
EDGEA="The connection betn the vetices."
""" tree is the special case of graph , the all connected element acyclic grpah is a tree"""

# Computer code:
from collections import deque

class GraphAdjList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, directed=False):
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = [False] * self.num_vertices
        order = []

        def dfs_util(v):
            visited[v] = True
            order.append(v)
            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start)
        return order

class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, directed=False):
        self.adj_matrix[u][v] = 1
        if not directed:
            self.adj_matrix[v][u] = 1

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[node][neighbor] and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = [False] * self.num_vertices
        order = []

        def dfs_util(v):
            visited[v] = True
            order.append(v)
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[v][neighbor] and not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start)
        return order

# Example usage and testing
if __name__ == "__main__":
    print("=== Graph (Adjacency List) Example ===")
    g_list = GraphAdjList(5)
    g_list.add_edge(0, 1)
    g_list.add_edge(0, 2)
    g_list.add_edge(1, 3)
    g_list.add_edge(1, 4)
    print("Adjacency List:", g_list.adj_list)
    print("BFS from 0:", g_list.bfs(0))
    print("DFS from 0:", g_list.dfs(0))

    print("\n=== Graph (Adjacency Matrix) Example ===")
    g_matrix = GraphAdjMatrix(5)
    g_matrix.add_edge(0, 1)
    g_matrix.add_edge(0, 2)
    g_matrix.add_edge(1, 3)
    g_matrix.add_edge(1, 4)
    print("Adjacency Matrix:")
    for row in g_matrix.adj_matrix:
        print(row)
    print("BFS from 0:", g_matrix.bfs(0))
    print("DFS from 0:", g_matrix.dfs(0))
