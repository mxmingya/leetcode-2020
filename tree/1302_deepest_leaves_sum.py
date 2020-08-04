# https://leetcode.com/problems/deepest-leaves-sum/discuss/771890/Python3-one-pass-recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.sum = 0
        self.maxHeight = 0;
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.helper(root, 0)
        return self.sum
        
    def helper(self, root, curHeight):
        if not root:
            return
        
        if curHeight == self.maxHeight:
            self.sum += root.val
        elif curHeight > self.maxHeight:
            self.maxHeight = curHeight
            self.sum = root.val
        
        # print(f"curHeight: {curHeight} sum: {self.sum}" )
        self.helper(root.left, curHeight + 1)
        self.helper(root.right, curHeight + 1)
        
#         deq = deque()
#         if root:
#             deq.append(root)
            
#         sum = 0
#         curHeight = 0
        
#         maxHeight = self.getHeight(root)
        
#         print(maxHeight)
        
#         while len(deq) > 0:
#             cur_node = deq.popleft()
#             curHeight += 1
#             if cur_node.left:
#                 deq.append(cur_node.left)
#             if cur_node.right:
#                 deq.append(cur_node.right)
            
#             if cur_node.left is None and cur_node.right is None:
                
#                 if curHeight == maxHeight:
#                     sum += cur_node.val
                    
#                 curHeight -= 1
            
#         return sum;
    
    
#     def getHeight(self, root: TreeNode):
#         if not root:
#             return 0;
#         return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        
