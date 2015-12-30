# My Pow function
# https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        # Recursion method
        
        flag = False
        if n<0:
            n *=-1
            flag = True
        if n==1:
            return x if not flag else 1/x
        elif n==0:
            return 1
        t = self.myPow(x,n/2)
        t = t*t if n%2==0 else x*t*t
        return 1/t if flag else t
        
        """
        #Iterative method
        flag = False
        if n<0:
            n *=-1
            flag = True
        ans = 1
        while n>0:
            if n&1 == 1:
                ans*=x
            x*=x
            n>>=1
        if flag:
            return 1/ans
        return ans