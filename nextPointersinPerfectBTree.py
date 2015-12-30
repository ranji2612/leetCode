# Populating Next Right Pointers in each Node in PERFECT Binary tree
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#### This is not a O(1) space solution
"""
class Solution(object):
    def connect(self, root):
        if root==None:
            return
        Q = []
        Q.append((root,0))
        while len(Q)>0:
            x,h = Q.pop(0)
            if x.left!=None:
                Q.append((x.left,h+1))
            if x.right!=None:
                Q.append((x.right,h+1))
            x.next = Q[0][0] if len(Q)>0 and Q[0][1]==h else None
"""

# O(1) Space solution
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root==None:
            return
        if root.left!=None:
            root.left.next = root.right
        if root.right!=None:
            root.right.next = root.next.left if root.next!=None else None
        self.connect(root.left)
        self.connect(root.right)