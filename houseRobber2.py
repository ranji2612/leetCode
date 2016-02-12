# House Robber 2
# https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def _rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        elif len(nums)==1:
            return nums[0]
        X = [0 for x in range(len(nums)+1)]
        X[1] = nums[0]
        X[2] = max(nums[0], nums[1])
        for i in range(3,len(nums)+1):
            X[i] = max(X[i-2]+nums[i-1], X[i-1])
        return X[-1]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self._rob(nums[1:]), self._rob(nums[2:-1])+nums[0]) if len(nums)>2 else self._rob(nums)