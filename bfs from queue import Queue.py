from queue import Queue

def bfs(graph, start):
    q = Queue()
    q.put(start)

    visited = {node: False for node in graph}
    parent = {node: None for node in graph}

    visited[start] = True

    print("BFS Order:", end=" ")
    while not q.empty():
        node = q.get()
        print(node, end=' ')

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.put(neighbor)

    print("\nPaths from start node:")
    for node in graph:
        path = []
        cur = node
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        print(f"Path to {node}: {path}")


# Example graph
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

bfs(graph, 0)
