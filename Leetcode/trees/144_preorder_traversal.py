# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC=O(n)  SC=O(n+h) n for ans and h for recursive calls
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root == None:
            return []
        self.ans = []
        return self.solve(root)

    def solve(self, node):
        if node == None:
            return
        self.ans.append(node.val)
        self.solve(node.left)
        self.solve(node.right)
        return self.ans
