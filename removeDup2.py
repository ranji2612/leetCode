# Remove duplicates from sorted array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=j=0
        prev = None
        c=0
        for i in range(len(nums)):
            if prev==nums[i]:
                c+=1
            else:
                c=1
                prev = nums[i]
            
            nums[j] = nums[i]
            if c<3:
                j+=1
        return j
            