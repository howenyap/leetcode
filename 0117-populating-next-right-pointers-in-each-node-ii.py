from collections import deque
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: Optional['Node'] = None, right: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        q = deque([root])

        while q:
            prev = None

            for _ in range(len(q)):
                node = q.popleft()

                for child in [node.left, node.right]:
                    if child:
                        q.append(child)

                if not prev:
                    prev = node
                else:
                    prev.next = node
                    prev = node

        return root
