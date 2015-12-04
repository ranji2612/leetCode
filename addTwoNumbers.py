# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = None
        head = None
        c = 0
        while l1 != None or l2 != None:
            s = c
            if l1 != None:
                s+= l1.val
                l1 = l1.next
            if l2 != None:
                s+= l2.val
                l2 = l2.next
            c = 1 if s > 9 else 0
            s = s%10
            if n == None:
                n = ListNode(s)
                head = n
            else:
                n.next = ListNode(s)
                n = n.next
        if c!=0:
            n.next = ListNode(c)
        return head
            