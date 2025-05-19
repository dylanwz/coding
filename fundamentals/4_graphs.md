# Graph
A graph is a structure representing a system with <mark style="background-color:#E5CCFF80">separate entities that are connected in some way</mark>. The entities are <i>nodes</i> and how they are connected is through <i>edges</i>.

They are associated with:
- representations,
- traversals,
- path finding (advanced),
- spanning trees (advanced).

### Representations
How to implemenet a graph? Two common, efficient approaches: adjacency list and adjacency matrix.

<mark style="background-color:#CCE5FF80">Adjacency List</mark>. For each node, record a list of other nodes adjacent to it.

```
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
```

It is space-efficient and easy to iterate over neigbours.

<mark style="background-color:#CCE5FF80">Adjacency Matrix</mark>. Each $(i,j)$ entry corresponds to the number of edges from node $i$ to $j$.

```
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
```

It is tailored to edge lookups; poorer space usage.

### Traversals
<mark style="background-color:#CCE5FF80">DFS</mark>. Go fully down (deep) one path before exploring others. Stack-based.

```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbour in graph[node]:
        dfs(neighbour, visited)
```
```python
def dfs(node):
    visited = set()
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(nighbour)
```

<mark style="background-color:#CCE5FF80">BFS</mark>. Go a bit down each path (breadth) in parallel. Queue-based.

```python
from collections import deque

def bfs(node):
    visited = set()
    queue = deque([node])

    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)