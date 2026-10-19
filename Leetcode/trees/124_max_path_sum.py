# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi = float("-inf")
        self.add(root)
        return self.maxi

    def add(self, node):
        if node == None:
            return 0
        leftsum = self.add(node.left)
        if leftsum < 0:
            leftsum = 0
        rightsum = self.add(node.right)
        if rightsum < 0:
            rightsum = 0
        self.maxi = max(self.maxi, leftsum + rightsum + node.val)
        return node.val + max(leftsum, rightsum)
