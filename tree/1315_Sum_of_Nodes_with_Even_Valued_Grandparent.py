# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.sum = 0
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        deq = deque()
        
        if root:
            deq.append(root)
            
        while len(deq) > 0:
            cur = deq.popleft()
            if cur.val % 2 == 0:
                # get grandchildren
        
                gc = self.getGrandChildren(cur)

                self.sum += sum(gc)
                
            if cur.left:
                deq.append(cur.left)
            if cur.right:
                deq.append(cur.right)

        
        return self.sum
                
                
                
    def getGrandChildren(self, root):
        c = []
        gc = []
        if root.left: 
            c.append(root.left)
        if root.right:
            c.append(root.right)
        
        for node in c:
            if node.left:
                gc.append(node.left.val)
            if node.right:
                gc.append(node.right.val)
        
        return gc
