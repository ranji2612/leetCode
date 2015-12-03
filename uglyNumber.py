# Ugly Number - https://leetcode.com/problems/ugly-number/
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in [2,3,5]:
            while num>0 and num%i==0:
                num/=i
        if num==1:
            return True
        return False