# Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)