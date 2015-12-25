# Kth Smallest Element in BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def getNoOfChild(n,x):
            
            if n==None:
                return 0,False
            
            lc,status = getNoOfChild(n.left,x)
            if status==True:
                return lc,True
            if x+lc+1==k:
                return n.val, True
            rc, status = getNoOfChild(n.right,x+lc+1)
            if status:
                return rc,True
            return lc + 1 + rc, False
        val, status = getNoOfChild(root,0)
        return val
            
        