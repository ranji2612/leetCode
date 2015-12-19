# Interleaving Strings
# https://leetcode.com/problems/interleaving-string/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # Basic Recursion - TLE Solution
        def chk(s,sa,sb):
            if len(s)==0:
                return True
            a = False
            b = False
            if len(sa)>0 and s[0]== sa[0]:
                a = chk(s[1:],sa[1:],sb)
            if len(sb)>0 and s[0] == sb[0]:
                b = chk(s[1:],sa,sb[1:])
            return a or b
        return chk(s3,s1,s2)