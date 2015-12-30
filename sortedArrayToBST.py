# Sorted Array to BST
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    l = len(nums)
    if l==0:
        return None
    m = l/2
    x = TreeNode(nums[m])
    x.left  = self.sortedArrayToBST(nums[:m])
    x.right = self.sortedArrayToBST(nums[m+1:])
    return x