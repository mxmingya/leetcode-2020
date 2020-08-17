# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.visited = set()
        
        def helper(root, prev):
            if root:
                self.visited.add(prev)
                helper(root.left, prev * 2 + 1)
                helper(root.right, prev * 2 + 2)
                
        helper(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.visited


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
