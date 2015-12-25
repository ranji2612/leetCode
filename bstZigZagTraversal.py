# Binary Tree ig-Zag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = []
        def addToList(n,k):
            if n==None:
                return
            if len(l)<=k:
                l.append([])
            l[k].append(n.val)
            addToList(n.left,k+1)
            addToList(n.right,k+1)
            return
        addToList(root,0)
        
        #Alternating
        i=0
        while i<len(l):
            if (i+1)%2==0:
                l[i] = l[i][::-1]
            i+=1
        return l