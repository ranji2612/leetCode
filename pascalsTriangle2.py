# Pascals Tricangle II
# https://leetcode.com/problems/pascals-triangle-ii/

#I think it can be optimized for time by using memoization

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def nck(n,k):
            k = min(k,n-k)
            i=1
            nu = 1
            de = 1
            while i<=k:
                nu*=(n-i+1)
                de*=i
                i+=1
            t = nu/de
            return t
        return [ nck(rowIndex,i) for i in range(rowIndex+1)]