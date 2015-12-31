# Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 0 if n==0 else 1
        N = [1,1,2,5]
        i=4
        while i<=n:
            a=0
            b=i-1
            s=0
            while a<=(i-1)/2:
                s+=N[a]*N[b]
                a+=1
                b-=1
            s<<=1
            if i&1==1:
                s-=(N[(i-1)/2]*N[(i-1)/2])
            N.append(s)
            i+=1
        return N[n]