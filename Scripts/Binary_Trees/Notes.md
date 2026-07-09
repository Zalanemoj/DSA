# 🌳 Binary Trees — Study Notes with Examples

> **Source:** DSA Python - Introduction to Binary Trees | Code and Debug (Part 106)

---

## 1. Hierarchical vs Linear Data Structures

**Linear** structures (arrays, linked lists, stacks, queues) store data sequentially.  
**Hierarchical** structures organize data in a parent-child relationship — like a tree.

**Real-world analogy:** A file system on your PC.

```
C:/
├── Documents/
│   ├── resume.pdf
│   └── notes.txt
├── Pictures/
│   └── vacation/
│       └── photo.jpg
└── Downloads/
```

Each folder is a **node**. `C:/` is the **root**. Sub-folders are **children**.

---

## 2. What is a Binary Tree?

A **Binary Tree** is a hierarchical data structure where each node has **at most 2 children** (left and right).

```
        5          ← Root Node
       / \
      3   2        ← Internal Nodes
     / \    \
    7   4    6     ← Leaf Nodes (no children)
```

| Children per Node | Valid in Binary Tree? |
|---|---|
| 0 | ✅ Yes (leaf node) |
| 1 | ✅ Yes |
| 2 | ✅ Yes |
| 3 or more | ❌ No — becomes a generic tree |

---

## 3. Core Terminology

### Example Tree

```
           10          ← Root
          /  \
         6    14
        / \     \
       4   8    20
              /
             17
```

| Term | Definition | Example (from tree above) |
|---|---|---|
| **Node** | Any element in the tree | `10`, `6`, `14`, `4`, `8`, `20`, `17` |
| **Root Node** | Top-most node; has no parent | `10` |
| **Children** | Direct nodes below a given node | Children of `6` → `4`, `8` |
| **Parent** | Direct node above a given node | Parent of `8` → `6` |
| **Leaf Node** | A node with 0 children | `4`, `8`, `17` |
| **Sub-tree** | Any node + all its descendants, acting as its own tree | `14 → 20 → 17` is a sub-tree |
| **Ancestors** | All nodes above a given node up to root | Ancestors of `17` → `20`, `14`, `10` |

---

## 4. Types of Binary Trees

---

### A. Full Binary Tree

> **Rule:** Every node has either **0 or 2 children**. No node has exactly 1 child.

```
✅ Full Binary Tree          ❌ NOT Full (node 3 has 1 child)

        1                          1
       / \                        / \
      2   3                      2   3
     / \                              \
    4   5                              5
```

**Key check:** Scan every node — if any node has exactly 1 child, it's not full.

---

### B. Complete Binary Tree

> **Rules:**
> 1. All levels are fully filled **except possibly the last**.
> 2. The last level is filled **left to right** with no gaps.

```
✅ Complete                  ❌ NOT Complete (gap on left)

        1                          1
       / \                        / \
      2   3                      2   3
     / \ /                          / \
    4  5 6                         5   6
```

**Practical use:** Binary Heaps (used in priority queues) are complete binary trees.

---

### C. Perfect Binary Tree

> **Rules:**
> 1. All **leaf nodes** are at the **same level**.
> 2. Every internal node has exactly **2 children**.

```
✅ Perfect Binary Tree

          1          ← Level 0
         / \
        2   3        ← Level 1
       / \ / \
      4  5 6  7      ← Level 2 (all leaves at same level)
```

**Formula:** A perfect binary tree of height `h` has `2^(h+1) - 1` total nodes.  
Example: Height = 2 → `2^3 - 1 = 7` nodes ✅

---

### D. Balanced Binary Tree

> **Rule:** For **every node**, the difference between the height of its left and right sub-trees is **at most 1**.
>
> `| Height(Left Subtree) - Height(Right Subtree) | ≤ 1`

```
✅ Balanced                  ❌ Unbalanced

      1                            1
     / \                          /
    2   3                        2
   /                            /
  4                            3
                              /
                             4

Height diff at node 1:        Height diff at node 1:
|2 - 1| = 1 ✅                |4 - 0| = 4 ❌
```

> ⚠️ You must verify the height difference at **every single node**, not just the root.

**Practical use:** AVL Trees and Red-Black Trees are self-balancing binary trees.

---

### E. Degenerate (Skewed) Binary Tree

> **Rule:** Every internal node has exactly **1 child**. Behaves like a linked list.

```
Left-Skewed:      Right-Skewed:

    1                  1
   /                    \
  2                      2
 /                        \
3                          3
 \
  4
```

**Problem:** Operations like search become O(n) instead of O(log n) — same as scanning a linked list. This is why balancing trees matters.

---

## 5. Quick Comparison Table

| Type | Every Node has | Last Level | Leaf Level |
|---|---|---|---|
| **Full** | 0 or 2 children | Any | Any |
| **Complete** | Any | Filled left to right | Any |
| **Perfect** | 2 children (internal) | Fully filled | All at same level |
| **Balanced** | Any | Any | `\|H_L - H_R\| ≤ 1` at every node |
| **Degenerate** | Exactly 1 child | N/A (linear) | At the bottom |

---

## 6. Python Implementation Preview

A binary tree node in Python is built using a class with OOP basics:

```python
class Node:
    def __init__(self, data):
        self.data = data       # The value stored in this node
        self.left = None       # Pointer to the left child
        self.right = None      # Pointer to the right child


# Build the tree manually:
#        10
#       /  \
#      6   14

root = Node(10)
root.left = Node(6)
root.right = Node(14)

print(root.data)        # 10
print(root.left.data)   # 6
print(root.right.data)  # 14
```

**Prerequisites:** Python classes, `__init__` constructor, and object instantiation.  
*(Inheritance and polymorphism are NOT required.)*

---

## 7. What's Coming Next

- Tree **Traversals**: Inorder, Preorder, Postorder, Level-order (BFS)
- Implementing each type of binary tree in Python
- Searching and inserting into binary trees

---