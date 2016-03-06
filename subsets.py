# Subsets
# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L = [[]]
        for i in nums:
            new = []
            for k in L:
                new.append(k+[i])
            L+=new
        return L