# 230. Kth Smallest Element in a BST

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def inOrder(node):
            if not node or len(res) >= k:
                return
            inOrder(node.left)
            if len(res) < k:
                res.append(node.val)
            inOrder(node.right)
        inOrder(root)
        # print(res)
        return res[k - 1]
            
# Helper function to build a binary tree from a list (BFS style)
def buildTree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root
