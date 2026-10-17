# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC=O(n)  SC=O(h) stackspace
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if self.count(root) != -1:
            return True
        return False

    def count(self, node):
        if node == None:
            return 0
        else:
            leftHeight = self.count(node.left)
            if leftHeight == -1:
                return -1
            rightHeight = self.count(node.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)
