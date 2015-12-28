# Count complete tree nodes 
# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leftHt(self, n):
        if n==None:
            return 0
        return 1 + self.leftHt(n.left)
        
    def rightHt(self, n):
        if n==None:
            return 0
        return 1 + self.rightHt(n.right)
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        lh = self.leftHt(root)
        rh = self.rightHt(root)
        if rh == lh:
            return int(math.pow(2,lh)) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
            