# sorted Linked List to BST
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if head==None:
        return None
    x   = head
    mid = head
    prev = head
    while x!=None and x.next!=None:
        prev = mid
        mid = mid.next
        x = x.next.next

    #print mid.val,x,prev.val
    prev.next = None
    t = TreeNode(mid.val)
    if head!=mid:
        t.left  = self.sortedListToBST(head)
    t.right = self.sortedListToBST(mid.next)
    return t
        