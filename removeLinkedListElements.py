# Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        x = head
        y = None
        head = None
        while x != None:
            if x.val != val:
                if y==None:
                    y = x
                    head = y
                else:
                    y.next = x
                    y = y.next
            x = x.next
        if y != None:
            y.next = None
        return head