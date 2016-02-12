
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        left = [ str(root.val)+'->'+x for x in self.binaryTreePaths(root.left)]
        right = [ str(root.val)+'->'+x for x in self.binaryTreePaths(root.right)]
        return left + right
        