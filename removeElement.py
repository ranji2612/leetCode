# Remove Element
# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = -1
        l = len(nums)
        i = 0
        while i <= l+c:
            if nums[i]==val:
                nums[i] = nums[c]
                c-=1
                continue
            i+=1
        return i