# Trees
A tree is a <mark style="background-color:#E5CCFF80">hierarchical, non-linear data structure</mark> with:
- One root node
- Parent-child relationships
- No cycles (unlike graphs)

They are associated with:
- construction,
- traversal,
- search,
- balancing.

### Construction
Define a class; each node is a parent with children.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Traversal
| Order         | Description         | Recursive Pattern                        |
| ------------- | ------------------- | ---------------------------------------- |
| **Inorder**   | Left → Root → Right | `dfs(node.left); visit; dfs(node.right)` |
| **Preorder**  | Root → Left → Right | `visit; dfs(node.left); dfs(node.right)` |
| **Postorder** | Left → Right → Root | `dfs(node.left); dfs(node.right); visit` |
| **Level Order** | Left → Right, layer-by-layer | `append(node.left); append(node.right); visit` |

M: the 'order' refers to where the root is

```
hashmap = {} // prefix sum base case
count = 0

for n in array:
    num_needed = k - n
    if hashmap[num_needed] > 0:
        count += hashmap[num_needed]
    hashmap[n] += 1

return count
```

### Search
In a BST,
- left subtree values < current
- right subtree values > greater.
Produces $\log(n)$ search time.
```python
def search_bst(node, target):
    if not node or node.val == target:
        return node
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

```

### Balancing
Balancing keeps the tree’s height = $O(\log n)$ for efficiency.

Why?
- A skewed BST becomes a linked list → slow operations.
- Balanced trees maintain fast $O(\log n)$ insert/search.

| Type               | Strategy                                                               |
| ------------------ | ---------------------------------------------------------------------- |
| **AVL Tree**       | Rotate nodes after insert/delete to maintain balance factor (−1, 0, 1) |
| **Red-Black Tree** | Allow some imbalance but recolor and rotate on violations              |
| **Splay Tree**     | Recently accessed nodes are moved near the root                        |
| **B-Trees**        | Generalize to M-ary trees; used in databases/disk storage              |
