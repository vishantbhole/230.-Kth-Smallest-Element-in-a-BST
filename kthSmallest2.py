# 230. Kth Smallest Element in a BST

from typing import Optional

import null


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


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

if __name__ == "__main__":
    sol = Solution()
    root = [3,1,4,None,2]
    k = 1
    print("Output is : ", sol.kthSmallest(buildTree(root), k))
