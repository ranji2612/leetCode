# Count Primes
# https://leetcode.com/problems/count-primes/

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Sieve of Eratosthenes
        if n<2:
            return 0
        s = [True for i in range(n)]
        s[0]=False
        s[1]=False
        x=2
        while x*x < n:
            p = x*x
            if s[p]==True:
                while p<n:
                    s[p] = False
                    p+=x
            x+=1
        #print s
        return sum(s)