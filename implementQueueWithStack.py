# Implement Queue using Stacks 
# https://leetcode.com/problems/implement-queue-using-stacks/

class Queue(object):
    q = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.q.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return False if len(self.q)>0 else True
        