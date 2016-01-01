# Partition List
# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        i = head
        h2 = j = None
        prev = None
        while i!=None:
            if i.val>=x:
                if j==None:
                    j = i
                    h2 = j
                else:
                    j.next = i
                    j = j.next
                if prev!=None:
                    prev.next = i.next
            else:
                if prev==None:
                    head = i
                prev = i
            i = i.next
        if prev!=None:
            prev.next = h2
        if j!=None:
            j.next = None
        return head