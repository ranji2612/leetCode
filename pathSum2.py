# PathSum 2
# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        if root.val == sum and root.left==None and root.right==None:
            return [[root.val]]
        x = self.pathSum(root.left, sum - root.val)+self.pathSum(root.right, sum - root.val)
        for i in range(len(x)):
            x[i].insert(0,root.val)
        return x
        