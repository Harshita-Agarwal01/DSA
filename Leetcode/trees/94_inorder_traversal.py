# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root==None:
            return []
        self.ans=[]
        return self.solve(root)
    def solve(self,node):
        if node==None:
            return
        self.solve(node.left)
        self.ans.append(node.val)
        self.solve(node.right)
        return self.ans
        