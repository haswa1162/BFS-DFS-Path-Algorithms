def dfs(graph, start):
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}

    stack = [start]

    print("DFS Order:", end=" ")
    while stack:
        current = stack.pop()

        if not visited[current]:
            print(current, end=' ')
            visited[current] = True

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    parent[neighbor] = current
                    stack.append(neighbor)

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

dfs(graph, 0)
