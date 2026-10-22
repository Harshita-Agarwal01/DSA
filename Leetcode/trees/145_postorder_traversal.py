# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root==None:
            return []
        self.ans=[]
        return self.solve(root)
    def solve(self,node):
        if node==None:
            return
        self.solve(node.left)
        self.solve(node.right)
        self.ans.append(node.val)
        return self.ans
        