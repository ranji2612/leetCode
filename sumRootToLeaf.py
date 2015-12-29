# Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tsum = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,s):
            if root==None:
                return
            if root.left==None and root.right==None:
                #print s+str(root.val)
                self.tsum+=int(s+str(root.val))
                return
            if root.left!=None:
                dfs(root.left, s+str(root.val))
            if root.right!=None:
                dfs(root.right, s+str(root.val))
        dfs(root,'')
        return self.tsum