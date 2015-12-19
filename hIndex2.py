# H - Index II
# https://leetcode.com/problems/h-index-ii/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        s = 0
        N = len(citations)
        e = N
        while s<e:
            m = (s+e)/2
            if citations[m] >= (N-m):
                e = m
            else:
                s = m + 1
        return N - s