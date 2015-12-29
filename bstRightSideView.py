# BST Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        Q = []
        res = []
        Q.append((root,0))
        while len(Q)>0:
            x,h = Q.pop(0)
            if len(res)<=h:
                res.append(x.val)
            if x.right!=None:
                Q.append((x.right,h+1))
            if x.left!=None:
                Q.append((x.left,h+1))
        return res