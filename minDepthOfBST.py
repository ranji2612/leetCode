# Minimum depth of binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root==None:
            return 0
        if root.right==None and root.left==None:
            return 1
        x1 = sys.maxint
        if root.right!=None:
            x1 = min(self.minDepth(root.right),x1)
        if root.left!=None:
            x1 = min(self.minDepth(root.left),x1)
        return x1+1
        