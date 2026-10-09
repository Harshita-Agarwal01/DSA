# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC=O(n)  SC=O(n) stack space
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.count(root)
        return self.diameter

    def count(self, node):
        if node == None:
            return 0

        leftHeight = self.count(node.left)

        rightHeight = self.count(node.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)
