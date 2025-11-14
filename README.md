This project contains modified versions of the BFS and DFS algorithms.  
The main goal was to edit both algorithms so they can print the path from the start node to every other node in the graph.

I added a parent tracking system in each algorithm, so after the traversal finishes, the code can reconstruct and print the path for every node.

There are two separate files:
1) bfs.py
2) dfs.py

Both files use the same example graph:

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

Each algorithm prints:
- The order of visiting nodes
- The path from the start node to every node

I also included a screenshot of the output as required.

This task was mainly about modifying BFS and DFS to show paths, and then uploading the code and the screenshot to GitHub.



<img width="1918" height="580" alt="Screenshot 2025-11-14 130640" src="https://github.com/user-attachments/assets/20ed727f-8bcd-4fdd-9c5f-8c9aea362f5d" />
