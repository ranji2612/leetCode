# First Bad Version
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        while s<n:
            m = (s+n)/2
            if isBadVersion(m):
                n = m
            else:
                s = m+1
        return s