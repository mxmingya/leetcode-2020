# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        self.i = 0
        def dfs(root, voyage):
            if not root:
                return True
            if root.val != voyage[self.i]:
                return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
            
            return dfs(root.left, voyage) & dfs(root.right, voyage)
        
        canFlip = dfs(root, voyage)
        
        return [-1] if not canFlip else res
