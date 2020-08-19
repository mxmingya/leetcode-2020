# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        def dfs(root, s):
            if not root:
                return s
            
            
            s = str(chr(root.val + 97)) + s
            
            if not root.left and not root.right:
                return s
            if not root.left and root.right:
                return dfs(root.right, s)
            if root.left and not root.right:
                return dfs(root.left, s)
            
            # print(f"smallest : {s} root: {chr(root.val + 97)}" )
            
            left = dfs(root.left, s)
            right = dfs(root.right, s)
            
            return left if left < right else right
        
        
        return dfs(root, "") 
