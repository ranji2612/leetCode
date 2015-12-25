# BST level order Trav II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
        return l[::-1]