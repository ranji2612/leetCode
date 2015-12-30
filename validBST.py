# Valid BST
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def inOrder(root,s,e):
        if root==None:
            return True
        if (not inOrder(root.left,s,root.val)) or (e!='inf' and root.val>=e) or (s!='-inf' and root.val<=s) or (not inOrder(root.right,root.val,e)):
            return False
        return True
    return inOrder(root,'-inf','inf')
            