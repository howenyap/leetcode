from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def traverse(root: Optional[TreeNode], acc: List[TreeNode]) -> List[TreeNode]:
            if not root:
                return acc

            acc.append(root)
            traverse(root.left, acc)
            traverse(root.right, acc)

            return acc

        nodes = traverse(root, list())

        if not nodes:
            return 

        prev = None

        for node in nodes:
            if not prev:
                prev = node
                prev.left = None
            else:
                prev.right = node
                prev = node
                prev.left = None

        return
        
