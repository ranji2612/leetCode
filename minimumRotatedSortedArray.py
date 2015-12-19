# Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        e=len(nums)-1
        if nums[s] <= nums[e]:
            return nums[0]
        while s<e-1:
            m = (s+e)/2
            if nums[m] > nums[e]:
                s = m
            else:
                e = m
        return nums[s+1]