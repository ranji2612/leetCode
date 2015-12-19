# H - Index
# https://leetcode.com/problems/h-index/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # I thought i'll use randomized partition to semisort every time i need to refer the mid point value by binary serch, but it passed with sorting itself. If you get TLE, then use rand partition which is better than sorting
        citations = sorted(citations)
        s = 0
        N = len(citations)
        e = N
        while s<e:
            m = (s+e)/2
            print m,citations[m]
            if citations[m] >= (N-m):
                e = m
            else:
                s = m + 1
        return N - s