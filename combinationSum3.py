# combination sum 3
# https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0 or k==0:
            return [[]] if n==0 and k==0 else []
        
        i=min(9,n- k*(k-1)/2)
        sc = int((math.sqrt(1+8*n)-1)/2)
        res = []
        while i>0 and i>=sc:
            if ( (k-1)*i - k*(k-1)/2 ) >= n-i:
                for x in self.combinationSum3(k-1,n-i):
                    if len(x)==0 or x[-1]<i:
                        res.append(x+[i])
            i-=1
        return res