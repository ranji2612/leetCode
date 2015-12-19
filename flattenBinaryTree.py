# Flatten a binary Tree
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def preOrder(a):
            if a==None:
                return []
            return [a.val] + preOrder(a.left) + preOrder(a.right)
        arr = preOrder(root)
        l = len(arr)
        if l > 1:
            root.val = arr[0]
            root.left = None
            root.right = None
            prev = root
            for i in range(1,l):
                prev.right = TreeNode(arr[i])
                prev = prev.right