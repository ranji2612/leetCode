# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = None
        start = x
        while l1!=None or l2!=None:
            if l2==None or (l1!=None and l1.val<= l2.val):
                if x==None:
                    x = l1
                    start = l1
                else:
                    x.next = l1
                    x = x.next
                l1 = l1.next
            else:
                if x==None:
                    x = l2
                    start = l2
                else:
                    x.next = l2
                    x = x.next
                l2 = l2.next
        return start
        
        