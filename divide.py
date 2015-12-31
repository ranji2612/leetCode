# Divide
# https://leetcode.com/problems/divide-two-integers/

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = False
        if dividend<0:
            dividend*=-1
            flag = not flag
        if divisor<0:
            divisor*=-1
            flag = not flag
        if dividend-divisor<0:
            return 0
        x = divisor
        l = 1
        while x<<1 <= dividend:
            l<<=1
            x<<=1
        l+=self.divide(dividend-x,divisor)
        
        l = -l if flag else l
        return 2147483647 if l>2147483647 else (-2147483648 if l<-2147483648 else l)