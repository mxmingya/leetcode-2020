# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class 1609_even_odd_tree(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque()
        level = 0
        q.append(root)
        
        while len(q) > 0:
            cur_len = len(q)
            is_odd_level = level % 2 == 1
            prev_node = None
            
            for i in range(0, cur_len):
                cur_node = q.popleft()
                if prev_node:
                    if is_odd_level:
                        if cur_node.val >= prev_node.val:
                            return False
                    else:
                        # even level
                        if cur_node.val <= prev_node.val:
                            return False
                
                if is_odd_level and cur_node.val % 2 == 1:
                    return False
                if not is_odd_level and cur_node.val % 2 == 0:
                    return False
                    
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                    
                prev_node = cur_node
                    
            level += 1
                    
        return True
                
                
