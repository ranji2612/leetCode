# Symmetric-Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def mirror(a,b):
            if a==None or b==None:
                return a==b
            return a.val==b.val and ( mirror(a.left,b.right) and mirror(a.right,b.left) )
        if root==None:
            return True
        return mirror(root.left,root.right)